# Prompt — Volume 2 of 5

Paste this entire message into a fresh claude.ai conversation. This is
**Volume 2 of a 5-volume reference document on LLM engineering**. Each
volume is rendered in its own conversation and produced as a separate,
standalone print-ready HTML artifact. Volumes share visual style so the
five PDFs look like one consistent series.

**This volume contains**: a brief volume opener and **Parts 4-6** —
Retrieval-Augmented Generation (beyond v1), Agentic systems, Inference
optimization & serving.

---

I want you to produce a **single, polished, print-ready HTML artifact**
titled **"LLM Engineering — A Practitioner's Reference · Volume 2"**.
I will save it as a PDF from my browser, so the document must be styled
for print. Treat this as a serious technical reference document — comparable
to a textbook chapter or a curated engineering handbook — for a working
machine-learning practitioner who already ships LLM-powered software and
wants a comprehensive reference covering modern, advanced, and
2025-2026-era LLM engineering.

This is **not** a tutorial for beginners and **not** a marketing document.
It is a dense, accurate, well-organized engineering reference.

---

## 1. Output format

- One **HTML artifact**, fully self-contained except for these CDN scripts:
  - Mermaid (`https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js`)
  - Prism.js core + autoloader for syntax highlighting
  - MathJax 3 for equations
- All CSS inline in a `<style>` block. No external CSS files.
- **Target length when printed: 24-30 A4 pages** for this volume.
- Renders correctly when opened in Chrome and printed via "Print → Save
  as PDF". Page-breaks, headers, footers, figure placement, and image
  containment must behave under print CSS.

## 2. Page, typography, color (identical across all five volumes)

```css
@page { size: A4; margin: 20mm 18mm 22mm 18mm; }
html { hyphens: auto; -webkit-hyphens: auto; }
*, *::before, *::after { box-sizing: border-box; }
body { text-align: left; }
p { margin: 0 0 8pt 0; }

@media print {
  /* Section / part breaks */
  .part { break-before: page !important; page-break-before: always !important; }

  /* Figures: hard absolute cap on height so they always fit one page. */
  figure {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
    max-height: 200mm;
    margin: 12pt 0 16pt 0;
  }
  figure .mermaid,
  figure .mermaid > svg,
  figure svg,
  figure img {
    max-width: 100% !important;
    max-height: 180mm !important;
    width: auto !important;
    height: auto !important;
    display: block;
    margin: 0 auto;
  }
  figcaption {
    break-before: avoid !important;
    page-break-before: avoid !important;
    margin-top: 6pt;
  }

  /* Code blocks: cap height, soft-wrap long lines, never split */
  pre {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
    max-height: 180mm;
    overflow: hidden;
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  /* Callouts and math display blocks */
  .callout, .math-display {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
  }

  /* Tables: header repeats, rows stay whole */
  table { break-inside: auto; }
  thead { display: table-header-group; }
  tfoot { display: table-footer-group; }
  tr, td, th {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
  }

  /* Headings keep with following content */
  h1, h2, h3, h4 {
    break-after: avoid !important;
    page-break-after: avoid !important;
    text-wrap: balance;
  }

  /* Section-opener banner stays attached to its first body content */
  .section-banner, .part-banner {
    break-after: avoid !important;
    page-break-after: avoid !important;
  }

  /* Widow / orphan control */
  p, li, dd { widows: 2; orphans: 2; }

  /* Hide screen-only elements */
  .no-print { display: none !important; }
}
```

The `<html>` root element must carry the attribute `lang="en"` for the
browser's hyphenation engine to engage.

> **Why these rules matter.** `break-inside: avoid` is only a hint; if
> an element is taller than the printable page area the browser must
> break it. The `!important` weight, the absolute-unit caps in mm, and
> the `figure svg { max-height: 180mm }` rule together prevent
> Mermaid's inline SVG sizing from overriding the cap.

- **Body**: `Inter, "Segoe UI", system-ui, -apple-system, sans-serif`,
  **12 pt**, line-height 1.55, color `#1A1A1A` on `#FFFFFF`,
  `text-align: left`, `hyphens: auto`. Paragraph spacing: 0 top, 8 pt
  bottom; no first-line indent.
- **Headings**: same family.
  - H1 (Part title): **32 pt**, weight 700, color `#0F2A4A`,
    line-height 1.15, `text-wrap: balance`.
  - H2 (Section): **20 pt**, weight 600, color `#0F2A4A`,
    24 pt top margin, 8 pt bottom margin, with a thin
    `1px solid #E5E9EF` bottom border and 6 pt of bottom padding.
  - H3 (Subsection): **14 pt**, weight 600, color `#1F6FEB`,
    18 pt top margin, 4 pt bottom margin.
- **Code**: `"JetBrains Mono", "Fira Code", Consolas, monospace`, **11 pt**,
  line-height 1.45, background `#F4F6FA`, padding 12 px, border-radius
  6 px. Language label in the top-right corner of each block, set in
  uppercase, 9 pt, tracked (`letter-spacing: 0.08em`), color `#4A5568`.
- **Inline code**: same monospace stack, 11 pt, `#F4F6FA` background,
  2 px horizontal padding, 4 px border-radius.
- **Figure captions** and other **muted text**: **10.5 pt**, color
  `#4A5568`; figure captions optionally italic.
- **Table captions**: **10.5 pt**, color `#4A5568`, placed *above* the
  table, prefixed `Table {part}.{n} · `.
- **Footnotes**: small superscript markers; footnote text **9.5 pt** at
  the bottom of the page they belong to. Number consistently per Part.
- **Running header / footer**: **9 pt**, color `#4A5568`.
- **Widow / orphan control**: minimum 2 lines on either side of a page
  break. Headings never end a page.
- **Color palette**:
  - Primary: `#0F2A4A` (deep navy)
  - Accent: `#1F6FEB` (blue)
  - Soft callout background: `#F4F6FA`
  - Success: `#1F8B4C`
  - Warning: `#B45309`
  - Muted text: `#4A5568`
- **Page header (running)**: small, muted, current Part name on the left,
  document title with " · Volume 2" on the right.
- **Page footer**: page number `counter(page) / counter(pages)` centered;
  small "Volume 2 of 5" on the left.
- **Volume opener page (page 1, no header/footer)**:
  - Top third of the page is whitespace.
  - A short horizontal accent rule, ~40 % page width, 2 px solid `#0F2A4A`,
    sitting just above the title.
  - Title: **LLM Engineering — A Practitioner's Reference**, **44 pt**,
    weight 700, navy.
  - Subtitle directly below: *Volume 2 · Retrieval · Agents ·
    Inference*, **16 pt**, weight 400, muted color `#4A5568`.
  - A tasteful decorative SVG element in the lower portion of the page.
  - Date line near the bottom: "2026 Edition", 11 pt, muted.
  - **No author, no logo, no personal details.**
- **Volume contents (page 2)**: list of the three Parts in this volume only,
  with leader dots and page numbers. Add a small "Companion volumes" note
  listing — by name only — what
  - Volume 1 (Parts 1-3: Foundations, Modern Model Landscape, Adapting
    Models)
  - Volume 3 (Parts 7-9: Production engineering, Evaluation, Safety &
    security)
  - Volume 4 (Parts 10-12: MLOps & LLMOps, Multimodal, System design
    playbook)
  - Volume 5 (Parts 13-15: Trends, Curated resources, Glossary)

  contain.

- **Section openers**: each Part begins on a new page with a full-width
  tinted banner (`#F4F6FA` background, `#0F2A4A` text, **3 px solid
  `#1F6FEB` left border**, 16 px vertical padding). Three lines:
  1. `PART N` in 11 pt uppercase tracked accent-blue.
  2. The Part title as H1 (32 pt navy).
  3. A one-sentence **italic "deck"** in 12.5 pt muted color.
- **Tables**: full-width by default; zebra striping (`#FAFBFD` alternate
  rows); no vertical rules; header row `#0F2A4A` background, white text,
  weight 600. Cell padding 8 px / 12 px. Caption sits **above**.
- **Callouts**: **Key idea** (blue left border), **Pitfall** (warning
  border), **Senior tip** (success border). Inline SVG icon, not emoji.
- **Figures**: numbered `Figure {part}.{n}`, caption below in muted text.

## 2.5 "How to save as PDF" callout (visible on screen, hidden in print)

At the very top of the rendered HTML — directly after the volume opener
— add a `<div class="no-print">` callout that the user sees on screen
but is hidden in print output. Style it the same as a "Key idea"
callout (soft `#F4F6FA` background, blue left border).

The callout text:

> **How to save this volume as a PDF.** Open this file in **Chrome** or
> Edge. Wait until every diagram and equation has finished rendering on
> screen. Press **Ctrl+P / ⌘P**. Set destination to **"Save as PDF"**.
> Under "More settings": **Margins → Default**, **Paper size → A4**,
> **Scale → Default (100 %)**, and **enable "Background graphics"** so
> banners and callout fills render. Then click **Save**.

## 3. Visualization & equation rendering — strict

- Every figure is a real visual: a **Mermaid** diagram or **inline SVG**.
- **No ASCII art, no box-drawing diagrams, no text-based figures.**
- SVGs are hand-written, with `viewBox` and labelled `<text>` elements;
  any text inside an SVG is at least 12 px.
- All figures have explicit captions placed below them.

### Mermaid configuration & legibility — non-negotiable

The printed page content area is ~174 mm wide. A flowchart with more
than five nodes laid out left-to-right becomes unreadable when scaled
to that width.

- **Initialize Mermaid once** near the top of the document with explicit
  config that sets a generous font size and the document palette:

  ```js
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'basis' },
    themeVariables: {
      fontFamily: 'Inter, "Segoe UI", system-ui, sans-serif',
      fontSize: '15px',
      primaryColor: '#F4F6FA',
      primaryBorderColor: '#0F2A4A',
      primaryTextColor: '#0F2A4A',
      lineColor: '#4A5568',
      secondaryColor: '#FFFFFF',
      tertiaryColor: '#E5E9EF'
    }
  });
  ```

- **Default to `flowchart TB`** (top-to-bottom). Use `flowchart LR` only
  when a diagram has at most five nodes total.
- **Never chain more than 5 nodes in a single row.** If a flow has more
  stages, switch direction or split into stacked subgraphs.
- **Do not unroll repeating structures.** Show one instance as a
  `subgraph` and mark multiplicity with a labeled loop-back edge or
  `× N` annotation on the subgraph border.
- **Use `subgraph` to group logically.** A pipeline with 3-5 stages
  appears as 3-5 subgraphs stacked top-to-bottom. **Limit to four
  subgraphs** per figure; if a flow needs more, split into Figure N.a /
  N.b.
- **Node labels stay short — at most about 3 words.**
- For **sequence diagrams**: at most ~5 participants and ~12 messages.
- For **mind-maps and graphs**: prefer `flowchart TB` with subgraphs.
- After drafting each diagram, mentally render it at ~174 mm wide and
  ask *"would labels stay readable in print, and would the diagram fit
  inside 180 mm of vertical space?"* If not, redesign.
- Always validate Mermaid syntax.

### Math rendering — non-negotiable

Every equation must render as proper math typography, never as raw
`$...$` source on the page.

- **Include MathJax 3 in the document `<head>`**, with the delimiter
  config defined BEFORE the loader script:

  ```html
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true
      },
      svg: { fontCache: 'global' },
      options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }
    };
  </script>
  <script id="MathJax-script" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
  ```

- **Render-completion guard** — add at the end of `<body>`:

  ```html
  <script>
    window.addEventListener('load', function() {
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise().catch(function(err) {
          console.error('MathJax typesetting failed:', err);
        });
      }
    });
  </script>
  ```

- **Use `\(...\)` for inline math and `$$...$$` for display math.** Do
  NOT use bare `$...$` for inline.
- **Display math goes in its own block.** Wrap in
  `<div class="math-display">$$ ... $$</div>` styled with
  `text-align: center`, 12 pt top/bottom margin, and
  `break-inside: avoid; page-break-inside: avoid`.
- **Heading + equation grouping**: wrap heading + paragraph + equation
  in a single `<div style="break-inside: avoid;
  page-break-inside: avoid;">`.
- **Never put math inside `<code>` or `<pre>`**, and never inside a
  markdown fenced code block.
- After drafting, scan every formula visually.

**Figures required in this volume:**

| #  | Figure                                                                  | Type                | Part |
|----|-------------------------------------------------------------------------|---------------------|------|
| 6  | Naive RAG vs Advanced RAG, side-by-side                                 | Mermaid flow        | 4    |
| 7  | GraphRAG / RAPTOR architecture                                          | Mermaid graph       | 4    |
| 8  | ReAct reasoning loop                                                    | Mermaid sequence    | 5    |
| 9  | Multi-agent state graph (LangGraph-style)                               | Mermaid graph       | 5    |
| 10 | Model Context Protocol: client ↔ server message flow                    | Mermaid sequence    | 5    |
| 11 | Inference stack: request → router → engine → KV cache                   | Mermaid graph       | 6    |
| 12 | Quantization formats compared (bits / quality / VRAM trade-offs)        | Inline SVG bar chart| 6    |

**Specific layout requirements for individual figures**

- **Figure 6** (Naive vs Advanced RAG) — render as **two separate
  `flowchart TB` blocks side-by-side** in a 2-column CSS grid (each
  column 50 % width; the print CSS will allow them to scale to 87 mm
  each). Three nodes per side max — keep it readable.
- **Figure 7** (GraphRAG / RAPTOR architecture) — `flowchart TB` with
  subgraphs separating ingestion, indexing, and retrieval stages. At
  most four subgraphs.
- **Figure 9** (multi-agent state graph) — `flowchart TB`; one node per
  agent role; edges labeled with hand-offs and conditions. At most
  five agent nodes.
- **Figure 11** (inference stack) — `flowchart TB` with stage subgraphs
  stacked vertically: request handling → routing → engine → KV cache.
  Each subgraph contains at most 3 nodes.

## 4. Content — what each Part must contain

### Part 4 — Retrieval-Augmented Generation, beyond v1 *(~9-10 pages)*
- Chunking strategies: fixed-size, recursive, semantic, late chunking,
  proposition-based.
- Hybrid retrieval (BM25 + dense), Reciprocal Rank Fusion.
- Reranking: cross-encoders, Cohere Rerank, ColBERT-v2.
- Query transformation: HyDE, multi-query, step-back prompting,
  sub-question decomposition.
- Advanced patterns: parent-document retrieval, contextual retrieval
  (Anthropic), GraphRAG, RAPTOR, Self-RAG, Corrective RAG, Agentic RAG.
- ANN index families: HNSW, IVF, IVF-PQ, ScaNN, FAISS internals; recall
  vs latency vs memory; when exact search still wins.
- Vector database landscape: Pinecone, Weaviate, Qdrant, Milvus, pgvector,
  LanceDB. Selection criteria.
- Multi-vector retrieval: ColBERT-v2 late interaction; ColPali for
  visual-document retrieval.
- Metadata filtering, time-decay / freshness, access-control filters.
- Document parsing tooling: Unstructured, LlamaParse, Docling, Marker —
  parsing quality often dominates retrieval quality.
- Embedding model selection (MTEB); domain fine-tuning of embeddings
  (contrastive, hard-negative mining).
- Include **Figure 6 and Figure 7**.
- Include a **20-line code snippet**: hybrid retrieval + cross-encoder
  rerank pipeline.

### Part 5 — Agentic systems *(~9-10 pages)*
- Patterns: ReAct, Plan-and-Execute, Reflexion, Tree-of-Thoughts, debate,
  router-agents.
- Frameworks: LangGraph, LlamaIndex Workflows, AutoGen, CrewAI, OpenAI
  Agents SDK, PydanticAI, smolagents — strengths and where each fits.
- Tool use and function calling: JSON Schema, structured outputs, parallel
  tool calls, JSON-mode quirks.
- Model Context Protocol (MCP): anatomy (clients, servers, transport),
  realistic use cases (filesystem, database, internal API access),
  security considerations.
- Memory systems: scratchpad, episodic, semantic, vector + graph memory,
  *context engineering*.
- Tool retrieval at scale: embedding tool descriptions and selecting the
  top-k tools when there are hundreds, instead of shoving all schemas into
  context.
- Computer-use / browser-control agents: Anthropic Computer Use, Operator-
  style approaches, Playwright-driven loops; unique failure modes
  (mis-clicks, drift).
- Agent sandboxing and security: prompt-injection defenses for agents
  differ from chat (the agent acts on the injection); least-privilege tool
  design, human-in-the-loop confirmation for destructive actions.
- Multi-agent orchestration: hierarchical, graph-based, blackboard.
- Evaluating agents: trajectory eval, tool-call accuracy, end-to-end
  success.
- Cost and latency budgets for agentic systems.
- Include **Figures 8, 9, 10**.
- Include a **20-line code snippet**: minimal LangGraph state graph with
  two nodes and a conditional edge.
- Include a **15-line code snippet**: minimal MCP server (Python).

### Part 6 — Inference optimization & serving *(~7-8 pages)*
- Engines: vLLM, TGI, TensorRT-LLM, SGLang, LMDeploy, llama.cpp, MLX,
  Ollama. Use cases.
- Quantization formats: BitsAndBytes 4/8-bit, GPTQ, AWQ, GGUF (Q4_K_M,
  Q5, Q8), SmoothQuant, FP8. Quality vs VRAM trade-off.
- KV-cache techniques: paged attention, prefix caching, KV reuse.
- Speculative-decoding family: vanilla draft-and-verify, Medusa, EAGLE /
  EAGLE-2, lookahead decoding, assisted generation — when each pays off.
- Disaggregated prefill / decode serving: separating compute-bound prefill
  from memory-bound decode for better utilization.
- Continuous batching, chunked prefill, FlashAttention 2 / 3.
- Distillation and pruning at a high level.
- Mixed-precision serving.
- Serving stacks: BentoML, Ray Serve, KServe, NVIDIA Triton, Modal,
  RunPod, Baseten.
- Capacity planning: tokens/sec, $/1M tokens, GPU sizing, throughput vs
  latency trade-offs.
- Include **Figures 11 and 12**.
- Include a **10-line shell snippet**: representative `vllm serve`
  command with quantization and tensor-parallel flags.

## 5. Code-snippet rules

- Each snippet stays between **10 and 30 lines**.
- Must be valid, runnable as written, using up-to-date APIs.
- No boilerplate scaffolding — only the conceptually important code.
- One-line caption above each snippet.
- Use Prism.js classes (`<pre><code class="language-python">…`).
- **No math inside any code block.**

## 6. Hard constraints

1. **One self-contained HTML artifact** for this volume. Inline CSS. CDN
   scripts only for Mermaid, Prism.js, MathJax 3.
2. **No ASCII art, no box-drawing diagrams, no text-based figures.**
3. **Technical accuracy first.** When unsure of a benchmark number,
   parameter count, or release date, describe qualitatively or omit.
   Never fabricate citations, URLs, or arXiv IDs.
4. **Consistent American English** throughout.
5. **No mention of interviews, hiring, jobs, candidates, CVs, recruitment,
   or any role-related framing.**
6. **No personal names, no logos, no company branding** beyond well-known
   public product names referenced for technical accuracy.
7. **Page-break discipline**: every Part starts on a new page; figures,
   code blocks, tables, and callouts must never be split across pages.
   Apply the print-CSS block in Section 2 exactly as written, including
   all `!important` weights and absolute-unit caps.
8. **Density discipline**: dense, information-rich prose. No filler.
9. **HTML root must carry `lang="en"`** so hyphenation engages.
10. **Every Part must open with a one-sentence italic deck line** under
    its title.
11. **This is Volume 2 of 5**. Render only Parts 4-6 in this artifact.
    Do not generate content for Parts 1-3 or 7-15.

## 7. Self-review pass before delivery

Before returning the artifact:

1. Re-read the document end-to-end.
2. Validate every Mermaid diagram: matching brackets; correct directives
   (`flowchart TB`, `sequenceDiagram`, `mindmap`); no row longer than
   5 nodes; at most 4 subgraphs per figure; repeating structures shown
   as a single `subgraph` with `× N`. Confirm `mermaid.initialize` is
   present with `fontSize: '15px'`.
3. Confirm Figures 6-12 are present and correctly numbered using
   `Figure {part}.{n}` (e.g., the first figure in Part 4 is
   `Figure 4.1`).
4. Confirm all required code snippets are present and within the line
   budget. Confirm no math inside any `<pre>`/`<code>`.
5. Sweep for grammar, spelling, agreement, consistent tense.
6. Sweep for any factual claim you are not confident about — soften or
   remove.
7. Sweep for any ASCII figure that may have slipped in.
8. **Print-CSS verification**: confirm the `@media print` block contains
   `!important` on every break/size rule, the figure
   `max-height: 200mm`, the `figure svg { max-height: 180mm !important }`
   rule, the `pre { max-height: 180mm; white-space: pre-wrap }`, the
   `thead { display: table-header-group }` rule, and the
   `tr { break-inside: avoid !important }` rule.
9. Confirm no mention of interviews, hiring, recruitment, or personal
   names.
10. Confirm every Part has its mandatory italic deck line.
11. Confirm `<html lang="en">` is set.
12. Confirm MathJax 3 is loaded in `<head>` with the inline-math
    delimiter config block placed BEFORE the loader script. Visually
    verify each equation renders as typeset math, never as raw
    `\(...\)` or `$$...$$` source. No math inside `<code>` or `<pre>`.
13. Confirm the screen-only "How to save as PDF" callout is present
    near the top, wrapped in `<div class="no-print">`.

Only then deliver.

---

**Begin now.** Output the complete Volume 2 HTML artifact.
