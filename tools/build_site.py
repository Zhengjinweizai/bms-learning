#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BMS 学习平台 — 本地阅读站点构建脚本（单文件离线站点）

用法：
    python3 tools/build_site.py
读取 knowledge/lessons/（77 门课）、knowledge/graph.md（77 节点登记）、
meta/pending-verification.md（待验证清单），生成 site/index.html。

- 纯标准库实现，无需安装依赖，生成的站点离线可用（双击打开）。
- 课程或图谱更新后重新运行本脚本即可刷新站点。
- 内部 .md 相对链接会被转换为站内跳转；http 链接新标签页打开。
- 阅读进度（已读标记）存在浏览器 localStorage，仅保存在本机。
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS_DIR = ROOT / "knowledge" / "lessons"
OUT_PATH = ROOT / "site" / "index.html"          # 本地离线版（gitignore）
OUT_PAGES = ROOT / "docs" / "index.html"         # GitHub Pages 版（入库并上线）

# 域元数据：key →（显示名，一句话说明）
DOMAINS = [
    ("ARCH", "跨域层 · 架构", "集中式 / 主从 / 分布式 / 无线 / 云边的取舍"),
    ("GEN", "跨域层 · 代际", "传统车载 → 云端辅助 → AI/数字孪生"),
    ("SYS", "域一 边界与架构", "BMS 管什么、管到哪、以什么形态挂上整车"),
    ("SAFE", "域二 安全设计", "ISO 26262 流程驱动 + 网络安全 + AI 论证"),
    ("HW", "域三 硬件", "AFE / MCU / 传感 / 隔离 / 执行"),
    ("SW", "域四 软件", "架构 / 调度 / 协议栈 / 状态机 / 诊断 / OTA"),
    ("HV", "域五 高压", "先建立、再维持、能撤出"),
    ("ALG", "域六 核心算法", "SOC / SOH / SOP / 均衡 / 诊断 / 模型"),
    ("CHG", "域七 充电", "接口 → 协议 → 控制 → 安全"),
    ("THM", "域八 热管理", "测得准 → 算得清 → 控得住"),
    ("FLT", "域九 故障", "识别 → 记录 → 降级 → 退出"),
    ("DEV", "域十 开发验证", "V 模型 / 验证阶梯 / HIL / 合规 / 标定"),
    ("CHM", "域十一 化学体系", "锂电基准 / 钠电 / 固态 / 梯次"),
]

# 最小可学习路径（与各域文件头部一致）
PATHS = [
    ("跨域层 · 架构", ["ARCH-C", "ARCH-MS", "ARCH-D", "ARCH-W", "ARCH-CE"], "线束成本/可靠性与控制权集中度的权衡，逐代松动"),
    ("跨域层 · 代际", ["GEN-1", "GEN-2", "GEN-3"], "算力从\"只在车上\"到\"车云分工\"再到\"模型驱动预测\""),
    ("SYS 边界与架构", ["SYS-01", "SYS-02", "ARCH-MS", "SYS-04", "SW-05"], "先知道 BMS 管什么、管到哪为止，再看形态"),
    ("SAFE 安全设计", ["SAFE-01", "SAFE-02", "SAFE-03", "SAFE-04"], "HARA 定目标，ASIL 定严格度，机制是落地——顺序不能反"),
    ("HW 硬件", ["HW-01", "HW-03", "HW-04", "HW-02", "HW-05"], "沿信号链：采集→传输→处理→执行"),
    ("SW 软件", ["SW-01", "SW-02", "SW-03", "SW-04", "SW-05"], "先立骨架，再通对外，后通行为"),
    ("HV 高压", ["HV-02", "HV-05", "HV-01", "HV-03", "HV-04"], "先建立、再维持、能撤出"),
    ("ALG 算法", ["ALG-01", "ALG-10", "ALG-02", "ALG-05", "ALG-06"], "模型是根，估计是干；状态→老化→能力"),
    ("CHG 充电", ["CHG-01", "CHG-02", "CHG-06", "CHG-03", "CHG-04"], "先物理连接，再对话，最后控制与安全底线"),
    ("THM 热管理", ["THM-01", "THM-02", "THM-03", "THM-04"], "先测得准，再算得清，再控得住"),
    ("FLT 故障", ["FLT-01", "FLT-02", "FLT-03", "FLT-04"], "识别→记录→降级→退出，四级递进"),
    ("DEV 开发验证", ["DEV-01", "DEV-02", "DEV-03", "DEV-04", "DEV-05"], "先流程后台架后法规，最后实车数据收口"),
]


def lesson_id_of(stem: str):
    m = re.match(r"^([A-Z]+-[A-Z0-9]+?)-", stem)
    return m.group(1) if m else None


# ---------- Markdown → HTML（覆盖本项目使用的子集） ----------

def make_inline(lesson_ids):
    def inline(s: str) -> str:
        spans = []

        def stash(m):
            spans.append(m.group(1))
            return "\x00%d\x00" % (len(spans) - 1)

        # 代码 span 与行内数学先摘出，避免内部被二次处理
        s = re.sub(r"`([^`]+)`", stash, s)
        s = re.sub(r"\$([^$]+)\$", stash, s)
        s = html.escape(s, quote=False)

        def link(m):
            text, url = m.group(1), m.group(2)
            if url.startswith("http"):
                return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, text)
            base = url.split("/")[-1]
            if base.endswith(".md"):
                lid = lesson_id_of(base[: -len(".md")])
                if lid and lid in lesson_ids:
                    return '<a class="xlink" href="#/lesson/%s">%s</a>' % (lid, text)
            return '%s <span class="fileref">（项目文件 %s）</span>' % (text, html.escape(url, quote=False))

        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
        s = re.sub(r"\x00(\d+)\x00", lambda m: "<code>%s</code>" % html.escape(spans[int(m.group(1))], quote=False), s)
        return s
    return inline


def md2html(md_text: str, lesson_ids) -> str:
    inline = make_inline(lesson_ids)
    lines = md_text.split("\n")
    out, para, list_type = [], [], None

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            para = []

    def flush_list():
        nonlocal list_type
        if list_type:
            out.append("</%s>" % list_type)
            list_type = None

    i, n = 0, len(lines)
    while i < n:
        raw = lines[i]
        s = raw.strip()
        # 原样放行的 HTML（details/summary 折叠块）
        if s.startswith("<details") or s.startswith("</details") or s.startswith("<summary") or s.startswith("</summary"):
            flush_para(); flush_list(); out.append(s)
            i += 1
            continue
        # 数学块（单行 $$...$$）
        if s.startswith("$$") and s.endswith("$$") and len(s) > 4:
            flush_para(); flush_list()
            out.append('<div class="math">%s</div>' % html.escape(s[2:-2].strip(), quote=False))
            i += 1
            continue
        # 分隔线
        if re.fullmatch(r"-{3,}", s):
            flush_para(); flush_list(); out.append("<hr>")
            i += 1
            continue
        # 标题
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush_para(); flush_list()
            lvl = min(len(m.group(1)) + 1, 5)  # 文件内 H1 降一级展示
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2)), lvl))
            i += 1
            continue
        # 表格
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            flush_para(); flush_list()
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            def cells(row):
                return [c.strip() for c in row.strip("|").split("|")]
            header = cells(rows[0])
            body_rows = [cells(r) for r in rows[2:]]
            t = ["<table>", "<thead><tr>"]
            t += ["<th>%s</th>" % inline(c) for c in header]
            t.append("</tr></thead><tbody>")
            for r in body_rows:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        # 引用块
        if s.startswith(">"):
            flush_para(); flush_list()
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote><p>%s</p></blockquote>" % inline(" ".join(q for q in quote if q)))
            continue
        # 列表
        m_ul = re.match(r"^(\s*)[-*]\s+(.*)$", raw)
        m_ol = re.match(r"^\s*\d+[.、]\s+(.*)$", raw)
        if m_ul or m_ol:
            flush_para()
            if m_ul:
                new_type, content = "ul", m_ul.group(2)
            else:
                new_type, content = "ol", m_ol.group(1)
            if list_type != new_type:
                flush_list()
                out.append("<%s>" % new_type)
                list_type = new_type
            out.append("<li>%s</li>" % inline(content))
            i += 1
            continue
        # 空行
        if not s:
            flush_para()
            i += 1
            continue
        # 普通段落（连续行合并）
        para.append(s)
        i += 1
    flush_para(); flush_list()
    return "\n".join(out)


# ---------- 数据收集 ----------

def collect_lessons():
    files = sorted(LESSONS_DIR.glob("*.md"))
    ids = set()
    for f in files:
        lid = lesson_id_of(f.stem)
        if lid:
            ids.add(lid)
    lessons = []
    for f in files:
        lid = lesson_id_of(f.stem)
        if not lid:
            continue
        text = f.read_text(encoding="utf-8")
        tm = re.search(r"^# (.+)$", text, re.M)
        title = tm.group(1).strip() if tm else f.stem
        body = re.sub(r"^# .+\n", "", text, count=1)
        rendered = md2html(body, ids)
        plain = re.sub(r"<[^>]+>", " ", rendered)
        plain = re.sub(r"\s+", " ", plain).lower()
        lessons.append({
            "id": lid,
            "title": title,
            "dom": lid.split("-")[0],
            "verified": lid in {"ALG-01", "ALG-10", "ALG-02", "ALG-05"},
            "html": rendered,
            "text": plain,
        })
    lessons.sort(key=lambda x: (x["dom"], x["id"]))
    return lessons


def collect_nodes():
    txt = (ROOT / "knowledge" / "graph.md").read_text(encoding="utf-8")
    nodes = []
    for line in txt.splitlines():
        s = line.strip()
        if not (s.startswith("|") and s.endswith("|")):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 7 and re.fullmatch(r"[A-Z]+-[A-Z0-9]+", cells[0]):
            nodes.append({"id": cells[0], "name": cells[1], "parent": cells[2],
                          "maturity": cells[3], "def": cells[4], "con": cells[5], "src": cells[6]})
    return nodes


def collect_pending():
    txt = (ROOT / "meta" / "pending-verification.md").read_text(encoding="utf-8")
    items = []
    for line in txt.splitlines():
        s = line.strip()
        if s.startswith("| P-") and s.endswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) >= 5:
                items.append({"id": cells[0], "item": cells[1], "status": cells[2],
                              "path": cells[3], "date": cells[4]})
    return items


def collect_conferences(lesson_ids):
    cdir = ROOT / "radar" / "conferences"
    confs = []
    for f in sorted(cdir.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        tm = re.search(r"^# (.+)$", text, re.M)
        title = tm.group(1).strip() if tm else f.stem
        body = re.sub(r"^# .+\n", "", text, count=1)
        rendered = md2html(body, lesson_ids)
        plain = re.sub(r"<[^>]+>", " ", rendered)
        plain = re.sub(r"\s+", " ", plain).lower()
        confs.append({"id": f.stem, "title": title, "html": rendered, "text": plain})
    return confs


def main():
    lessons = collect_lessons()
    nodes = collect_nodes()
    pending = collect_pending()
    confs = collect_conferences({l["id"] for l in lessons})
    data = {
        "domains": [{"key": k, "name": n, "desc": d} for k, n, d in DOMAINS],
        "paths": [{"name": p, "ids": ids, "logic": logic} for p, ids, logic in PATHS],
        "lessons": lessons,
        "nodes": nodes,
        "pending": pending,
        "conferences": confs,
        "built": "2026-11-04",
    }
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    page = TEMPLATE.replace("__DATA__", payload)
    OUT_PATH.parent.mkdir(exist_ok=True)
    OUT_PATH.write_text(page, encoding="utf-8")
    OUT_PAGES.parent.mkdir(exist_ok=True)
    OUT_PAGES.write_text(page, encoding="utf-8")
    size_kb = OUT_PATH.stat().st_size / 1024
    print("OK  site/index.html      %.0f KB  | 课程 %d 门 | 节点 %d | 待验证 %d"
          % (size_kb, len(lessons), len(nodes), len(pending)))
    print("OK  docs/index.html（GitHub Pages 同步）")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>BMS 学习平台 · 阅读站</title>
<style>
:root{
  --bg:#f6f7f9; --panel:#ffffff; --fg:#1c2330; --muted:#6b7686; --line:#e4e8ee;
  --accent:#2563eb; --accent-soft:#eaf1fe; --ok:#15803d; --warn:#b45309; --front:#7c3aed;
  --code-bg:#f1f3f7;
}
@media (prefers-color-scheme: dark){
  :root{ --bg:#14181f; --panel:#1c2129; --fg:#e7ebf1; --muted:#96a0ae; --line:#2a313c;
    --accent:#6ea8fe; --accent-soft:#1d2a3f; --ok:#4ade80; --warn:#fbbf24; --front:#c4b5fd;
    --code-bg:#242b36; }
}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  background:var(--bg);color:var(--fg);font-size:15px;line-height:1.75}
#app{display:flex;min-height:100vh}
aside{width:288px;flex:0 0 288px;background:var(--panel);border-right:1px solid var(--line);
  height:100vh;position:sticky;top:0;display:flex;flex-direction:column}
.logo{padding:16px 18px 10px}
.logo b{font-size:16px}
.logo .sub{color:var(--muted);font-size:12px;margin-top:2px}
.viewtabs{display:flex;gap:6px;padding:8px 14px;border-bottom:1px solid var(--line)}
.viewtabs button{flex:1;border:1px solid var(--line);background:transparent;color:var(--muted);
  border-radius:8px;padding:6px 0;font-size:13px;cursor:pointer}
.viewtabs button.active{background:var(--accent-soft);color:var(--accent);border-color:var(--accent);font-weight:600}
#search{margin:10px 14px 6px;padding:8px 10px;border:1px solid var(--line);border-radius:8px;
  background:var(--bg);color:var(--fg);font-size:13px;width:calc(100% - 28px)}
#nav{overflow-y:auto;flex:1;padding:6px 8px 90px}
.dom{margin-top:10px}
.dom-h{display:flex;justify-content:space-between;align-items:baseline;padding:4px 10px;color:var(--muted);font-size:12px}
.dom-h b{color:var(--fg);font-size:13px;font-weight:600}
.les{display:flex;align-items:center;gap:7px;width:100%;text-align:left;border:0;background:none;
  color:var(--fg);font:inherit;font-size:13px;padding:5px 10px;border-radius:8px;cursor:pointer}
.les:hover{background:var(--accent-soft)}
.les.active{background:var(--accent-soft);color:var(--accent);font-weight:600}
.les .lid{color:var(--muted);font-size:11px;flex:0 0 62px}
.les .tt{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.les .rd{flex:0 0 auto;width:7px;height:7px;border-radius:50%;background:transparent;border:1.5px solid var(--line)}
.les.isread .rd{background:var(--ok);border-color:var(--ok)}
.progress{position:absolute;bottom:0;left:0;right:0;padding:10px 16px;border-top:1px solid var(--line);
  background:var(--panel);font-size:12px;color:var(--muted)}
main{flex:1;min-width:0;padding:28px 34px 80px}
.wrap{max-width:860px;margin:0 auto}
.crumb{color:var(--muted);font-size:12.5px;margin-bottom:6px}
.content{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:26px 30px}
.content h2{font-size:20px;margin:28px 0 10px;padding-top:14px;border-top:1px solid var(--line)}
.content h2:first-child{margin-top:0;border-top:0;padding-top:0}
.content h3{font-size:16.5px;margin:22px 0 8px}
.content table{border-collapse:collapse;width:100%;margin:12px 0;font-size:13.5px}
.content th,.content td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
.content th{background:var(--accent-soft);font-weight:600}
.content code{background:var(--code-bg);border-radius:5px;padding:1px 6px;font-size:13px;
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.content pre{background:var(--code-bg);border-radius:8px;padding:12px 14px;overflow-x:auto}
.content blockquote{border-left:3px solid var(--accent);background:var(--accent-soft);
  margin:12px 0;padding:8px 14px;border-radius:0 8px 8px 0;color:var(--muted)}
.content details{border:1px solid var(--line);border-radius:10px;padding:8px 14px;margin:10px 0;background:var(--bg)}
.content summary{cursor:pointer;font-weight:600;color:var(--accent)}
.content .math{background:var(--code-bg);border-radius:8px;padding:10px 14px;margin:10px 0;
  font-family:ui-monospace,Menlo,monospace;font-size:13.5px;overflow-x:auto}
.content a{color:var(--accent);text-decoration:none}
.content a:hover{text-decoration:underline}
.content li{margin:3px 0}
.fileref{color:var(--muted);font-size:12px}
.badge{display:inline-block;padding:1px 9px;border-radius:999px;font-size:11.5px;font-weight:600;margin-right:6px}
.b-stable{background:rgba(21,128,61,.13);color:var(--ok)}
.b-evolving{background:rgba(180,83,9,.13);color:var(--warn)}
.b-frontier{background:rgba(124,58,237,.13);color:var(--front)}
.b-acc{background:var(--accent-soft);color:var(--accent)}
.lesstop{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:4px}
.readbtn{border:1px solid var(--line);background:transparent;color:var(--muted);border-radius:8px;
  padding:5px 12px;font-size:12.5px;cursor:pointer}
.readbtn.on{background:var(--ok);border-color:var(--ok);color:#fff}
.pn{display:flex;justify-content:space-between;gap:10px;margin-top:18px}
.pn button{border:1px solid var(--line);background:var(--panel);color:var(--fg);border-radius:10px;
  padding:8px 14px;font-size:13px;cursor:pointer;max-width:48%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pn button:hover{border-color:var(--accent);color:var(--accent)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(255px,1fr));gap:12px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:13px 15px}
.card h4{margin:0 0 6px;font-size:14px}
.card p{margin:4px 0;font-size:13px;color:var(--muted)}
.pathstep{display:inline-block;background:var(--accent-soft);color:var(--accent);border-radius:7px;
  padding:2px 9px;font-size:12.5px;margin:2px 3px 2px 0}
.empty{color:var(--muted);text-align:center;padding:40px 0}
.hitmark{background:#ffe89c;color:inherit;border-radius:3px}
@media (max-width:860px){
  #app{flex-direction:column}
  aside{width:100%;flex:none;height:auto;position:static;border-right:0;border-bottom:1px solid var(--line)}
  #nav{max-height:40vh}
  main{padding:18px 14px 60px}
  .content{padding:18px 16px}
}
</style>
</head>
<body>
<div id="app">
  <aside>
    <div class="logo"><b>⚡ BMS 学习平台</b><div class="sub">77 节点 · 77 课 · 离线阅读站</div></div>
    <div class="viewtabs" id="viewtabs"></div>
    <input id="search" type="search" placeholder="全文搜索（课程/节点/待验证）…">
    <div id="nav"></div>
    <div class="progress" id="progress"></div>
  </aside>
  <main><div class="wrap" id="main"></div></main>
</div>
<script>
const DATA = __DATA__;
const BYID = {}; DATA.lessons.forEach(l => BYID[l.id] = l);
const $ = s => document.querySelector(s);
const esc = s => s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
const READ = JSON.parse(localStorage.getItem("bmsRead") || "{}");
const VIEWS = [["lesson","📚 课程"],["tree","🌳 知识树"],["paths","🧭 学习路径"],["conf","🎓 会议"],["pending","🔍 待验证"]];
let view = "lesson", current = null, q = "";

function saveRead(){ localStorage.setItem("bmsRead", JSON.stringify(READ)); }
function matBadge(m){ const c = m==="stable"?"b-stable":(m==="evolving"?"b-evolving":"b-frontier");
  const z = m==="stable"?"stable":(m==="evolving"?"evolving":"frontier"); return '<span class="badge '+c+'">'+z+'</span>'; }
function lessonPath(d){ let arr=[]; DATA.domains.forEach(dm=>arr=arr.concat(DATA.lessons.filter(l=>l.dom===dm.key))); return arr; }
const ORDER = lessonPath();

function renderTabs(){
  $("#viewtabs").innerHTML = VIEWS.map(v =>
    '<button data-v="'+v[0]+'" class="'+(view===v[0]?"active":"")+'">'+v[1]+'</button>').join("");
}
function renderNav(){
  const nav = $("#nav"); let html = "";
  const ql = q.trim().toLowerCase();
  if(view === "lesson"){
    DATA.domains.forEach(dm => {
      const les = DATA.lessons.filter(l => l.dom === dm.key &&
        (!ql || (l.id+" "+l.title+" "+l.text).toLowerCase().includes(ql)));
      if(!les.length) return;
      html += '<div class="dom"><div class="dom-h"><b>'+dm.name+'</b><span>'+les.length+'/'+
        DATA.lessons.filter(l=>l.dom===dm.key).length+'</span></div>' +
        les.map(l => '<button class="les '+(current===l.id?"active ":"")+(READ[l.id]?"isread":"")+
          '" data-id="'+l.id+'"><span class="rd"></span><span class="lid">'+l.id+
          '</span><span class="tt">'+esc(l.title)+'</span></button>').join("") + '</div>';
    });
  } else if(view === "tree"){
    DATA.domains.forEach(dm => {
      const ns = DATA.nodes.filter(nd => nd.id.startsWith(dm.key) &&
        (!ql || (nd.id+" "+nd.name+" "+nd.def).toLowerCase().includes(ql)));
      if(!ns.length) return;
      html += '<div class="dom"><div class="dom-h"><b>'+dm.name+'</b><span>'+ns.length+'</span></div>' +
        ns.map(nd => '<button class="les" data-node="'+nd.id+'"><span class="lid">'+nd.id+
          '</span><span class="tt">'+esc(nd.name)+'</span></button>').join("") + '</div>';
    });
  } else if(view === "conf"){
    const cs = DATA.conferences.filter(c => !ql || (c.id+" "+c.title+" "+c.text).toLowerCase().includes(ql));
    html = '<div class="dom"><div class="dom-h"><b>会议与项目条目</b><span>'+cs.length+'</span></div>' +
      cs.map(c => '<button class="les" data-conf="'+c.id+'"><span class="tt" style="flex:1">'+esc(c.title)+'</span></button>').join("") + '</div>';
  } else if(view === "pending"){
    const ps = DATA.pending.filter(p => !ql || (p.id+" "+p.item).toLowerCase().includes(ql));
    html = '<div class="dom"><div class="dom-h"><b>待验证清单</b><span>'+ps.length+'</span></div>' +
      ps.map(p => '<button class="les" data-pend="'+p.id+'"><span class="lid">'+p.id+
        '</span><span class="tt">'+esc(p.item.slice(0,26))+'…</span></button>').join("") + '</div>';
  }
  nav.innerHTML = html || '<div class="empty">无匹配结果</div>';
  const total = DATA.lessons.length, done = Object.keys(READ).length;
  $("#progress").textContent = "阅读进度：" + done + " / " + total + " 课（" + Math.round(done/total*100) + "%）";
}
function markBtn(id){
  return '<button class="readbtn '+(READ[id]?"on":"")+'" id="readtoggle">'+(READ[id]?"✓ 已读":"标记已读")+'</button>';
}
function showLesson(id){
  const l = BYID[id]; if(!l) return;
  const dm = DATA.domains.find(d => d.key === l.dom);
  const idx = ORDER.findIndex(x => x.id === id);
  const prev = idx > 0 ? ORDER[idx-1] : null, next = idx < ORDER.length-1 ? ORDER[idx+1] : null;
  $("#main").innerHTML =
    '<div class="crumb">'+dm.name+' · '+l.id+(l.verified?' <span class="badge b-stable">延伸资源已核实</span>':'')+'</div>' +
    '<div class="content"><div class="lesstop"><h2 style="border:0;padding:0;margin:0 0 4px">'+esc(l.title)+'</h2>'+markBtn(id)+'</div>'+
    l.html + '</div>' +
    '<div class="pn">'+(prev?'<button data-go="'+prev.id+'">← '+prev.id+'</button>':'<span></span>')+
    (next?'<button data-go="'+next.id+'">'+next.id+' →</button>':'<span></span>')+'</div>';
  current = id; window.scrollTo(0,0);
}
function showTree(){
  $("#main").innerHTML = '<div class="content"><h2 style="border:0;margin-top:0">知识树（77 节点）</h2>' +
    '<p style="color:var(--muted)">卡片来自 v0.1.0 登记表；约束为骨架期常识层，逐条溯源见项目 sources/。</p>' +
    DATA.domains.map(dm => {
      const ns = DATA.nodes.filter(nd => nd.id.startsWith(dm.key));
      if(!ns.length) return "";
      return '<h3>'+dm.name+' <span style="color:var(--muted);font-size:12px">'+dm.desc+'</span></h3>' +
        '<div class="grid">'+ns.map(nd =>
          '<div class="card"><h4>'+nd.id+' · '+esc(nd.name)+' '+matBadge(nd.maturity)+'</h4>'+
          '<p>'+esc(nd.def)+'</p><p><b style="color:var(--fg)">约束：</b>'+esc(nd.con)+'</p></div>').join("")+'</div>';
    }).join("") + '</div>';
  window.scrollTo(0,0);
}
function showPaths(){
  $("#main").innerHTML = '<div class="content"><h2 style="border:0;margin-top:0">最小学习路径（12 条）</h2>' +
    DATA.paths.map(p => '<h3>'+p.name+'</h3><div>'+
      p.ids.map(id => '<a class="pathstep" href="#/lesson/'+id+'" style="text-decoration:none">'+id+'</a>').join('<span style="color:var(--muted)">→</span>')+
      '</div><p style="color:var(--muted);font-size:13px;margin:6px 0 18px">'+esc(p.logic)+'</p>').join("") + '</div>';
  window.scrollTo(0,0);
}
function showPending(focus){
  $("#main").innerHTML = '<div class="content"><h2 style="border:0;margin-top:0">待验证清单（'+DATA.pending.length+' 项）</h2>' +
    '<p style="color:var(--muted)">诚实机制的出口：所有"有线索但证据不足"的表述登记于此，核对后并入知识库。</p>' +
    '<table><thead><tr><th>编号</th><th>内容</th><th>状态</th><th>验证路径</th></tr></thead><tbody>' +
    DATA.pending.map(p => '<tr id="p-'+p.id+'" style="'+(focus===p.id?"outline:2px solid var(--accent)":"")+
      '"><td><b>'+p.id+'</b></td><td>'+esc(p.item)+'</td><td>'+esc(p.status)+'</td><td>'+esc(p.path)+'</td></tr>').join("") +
    '</tbody></table></div>';
  window.scrollTo(0,0);
}
function showConf(cid){
  const c = DATA.conferences.find(x => x.id === cid); if(!c) return;
  $("#main").innerHTML = '<div class="crumb">会议追踪 · radar/conferences/</div><div class="content">'+c.html+'</div>';
  window.scrollTo(0,0);
}
function route(){
  const h = location.hash.replace(/^#\/?/, "");
  if(h.startsWith("lesson/")){ view="lesson"; showLesson(h.slice(7)); }
  else if(h === "tree"){ view="tree"; showTree(); }
  else if(h === "paths"){ view="paths"; showPaths(); }
  else if(h === "conf"){ view="conf"; showConf(DATA.conferences[0].id); }
  else if(h.startsWith("conf/")){ view="conf"; showConf(h.slice(5)); }
  else if(h.startsWith("pending")){ view="pending"; showPending(h.split("/")[1]); }
  else { view="lesson"; if(!current) current = ORDER[0] ? ORDER[0].id : null; if(current) showLesson(current); }
  renderTabs(); renderNav();
}
document.addEventListener("click", e => {
  const t = e.target.closest("button, a.pathstep, a.xlink");
  if(!t) return;
  if(t.dataset.v){ location.hash = t.dataset.v === "lesson" ? "#/lesson/"+(current||ORDER[0].id) : "#/"+t.dataset.v; return; }
  if(t.dataset.id){ location.hash = "#/lesson/"+t.dataset.id; return; }
  if(t.dataset.node){ const nd = DATA.nodes.find(x=>x.id===t.dataset.node);
    $("#main").innerHTML='<div class="content"><div class="crumb">知识树 · '+nd.id+' · '+matBadge(nd.maturity)+'</div>'+
      '<h2 style="border:0;margin-top:0">'+esc(nd.name)+'</h2><p>'+esc(nd.def)+'</p><p><b>关键约束：</b>'+esc(nd.con)+
      '</p><p style="color:var(--muted);font-size:13px">来源：'+esc(nd.src)+'（meta/source-registry.md）</p></div>';
    window.scrollTo(0,0); return; }
  if(t.dataset.pend){ view="pending"; renderTabs(); renderNav(); showPending(t.dataset.pend); return; }
  if(t.dataset.conf){ location.hash = "#/conf/"+t.dataset.conf; return; }
  if(t.dataset.go){ location.hash = "#/lesson/"+t.dataset.go; return; }
  if(t.id === "readtoggle"){ READ[current] = !READ[current]; if(!READ[current]) delete READ[current];
    saveRead(); showLesson(current); renderNav(); return; }
});
$("#search").addEventListener("input", e => { q = e.target.value; renderNav(); });
window.addEventListener("hashchange", route);
route();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
