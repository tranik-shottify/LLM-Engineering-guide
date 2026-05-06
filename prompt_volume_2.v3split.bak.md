# Prompt — Volume 2 of 3

Paste this entire message into a fresh claude.ai conversation. This is
**Volume 2 of a 3-volume reference document on LLM engineering**. Each
volume is rendered in its own conversation and produced as a separate,
standalone print-ready HTML artifact. Volumes share visual style so the
three PDFs look like one consistent series.

**This volume contains**: a brief volume opener and **Parts 6-10** —
Inference optimization & serving, Production engineering for LLM apps,
Evaluation, Safety / security / responsible AI, MLOps & LLMOps.

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
  - Optionally MathJax for any math
- All CSS inline in a `<style>` block. No external CSS files.
- **Target length when printed: 26-32 A4 pages** for this volume.
- Renders correctly when opened in Chrome and printed via "Print → Save
  as PDF".

## 2. Page, typography, color (identical across all three volumes)

```css
@page { size: A4; margin: 18mm 18mm 20mm 18mm; }
html { hyphens: auto; -webkit-hyphens: auto; }
body { text-align: left; }
p { margin: 0 0 8pt 0; }
@media print {
  .part { break-before: page; }
  figure, pre, .callout, table { break-inside: avoid; page-break-inside: avoid; }
  h1, h2, h3 { break-after: avoid; text-wrap: balance; }
  p, li, dd { widows: 2; orphans: 2; }
  figure .mermaid svg, figure svg { max-height: 650px; width: auto; }
  .math-display { break-inside: avoid; page-break-inside: avoid; }
}
```

The `<html>` root element must carry the attribute `lang="en"` for the
browser's hyphenation engine to engage.

- **Body**: `Inter, "Segoe UI", system-ui, -apple-system, sans-serif`,
  **12 pt**, line-height 1.55, color `#1A1A1A` on `#FFFFFF`,
  `text-align: left`, `hyphens: auto` (rag-right and hyphenated, like a
  proper book — never fully justified). Paragraph spacing: 0 top, 8 pt
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
  2 px horizontal padding, 4 px border-radius — visually unified with
  block code.
- **Figure captions** and other **muted text**: **10.5 pt**, color
  `#4A5568`; figure captions optionally italic.
- **Table captions**: **10.5 pt**, color `#4A5568`, placed *above* the
  table, prefixed `Table {part}.{n} · ` (matching the figure scheme).
- **Footnotes**: small superscript markers in body
  (`<sup class="fn-ref">`); footnote text **9.5 pt** at the bottom of
  the page they belong to. Number consistently per Part.
- **Running header / footer**: **9 pt**, color `#4A5568`.
- **Widow / orphan control**: minimum 2 lines of any paragraph or list
  on either side of a page break. Headings never end a page.
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
  small "Volume 2 of 3" on the left.
- **Volume opener page (page 1, no header/footer)**:
  - Top third of the page is whitespace.
  - A short horizontal accent rule, ~40 % page width, 2 px solid `#0F2A4A`,
    sitting just above the title.
  - Title: **LLM Engineering — A Practitioner's Reference**, **44 pt**,
    weight 700, navy, balanced wrapping.
  - Subtitle directly below: *Volume 2 · Inference · Production ·
    Evaluation · Safety · LLMOps*, **16 pt**, weight 400, muted
    color `#4A5568`.
  - A tasteful decorative SVG element in the lower portion of the page —
    a thin geometric band or angled stripes in `#0F2A4A` and `#1F6FEB`.
    Restrained, not loud.
  - Date line near the bottom: "2026 Edition", 11 pt, muted.
  - **No author, no logo, no personal details.**
- **Volume contents (page 2)**: list of the five Parts in this volume only,
  with leader dots and page numbers. Add a small "Companion volumes" note
  listing — by name only — what Volume 1 (Parts 1-5: Foundations, Modern
  Model Landscape, Adapting Models, RAG, Agents) and Volume 3 (Parts
  11-15: Multimodal, System Design, Trends, Resources, Glossary) contain.
- **Section openers**: each Part begins on a new page with a full-width
  tinted banner (`#F4F6FA` background, `#0F2A4A` text, **3 px solid
  `#1F6FEB` left border**, 16 px vertical padding). The banner contains
  three lines, top to bottom:
  1. `PART N` in 11 pt uppercase tracked accent-blue.
  2. The Part title as H1 (32 pt navy).
  3. A one-sentence **italic "deck"** in 12.5 pt muted color (`#4A5568`)
     summarizing what the Part covers — for example, *"Vocabulary fixed
     in nine pages: enough to make the rest of the document
     unambiguous."* Write a fresh deck for every Part. This is a
     mandatory book-craft element, not optional.
- **Tables**: full-width by default; zebra striping (`#FAFBFD` alternate
  rows); no vertical rules; header row `#0F2A4A` background, white text,
  weight 600. Cell padding 8 px vertical, 12 px horizontal. Thin
  `1 px solid #E5E9EF` rule below the header and at the bottom of the
  table. Caption sits **above** the table per the table-caption spec.
- **Callouts**: **Key idea** (blue left border), **Pitfall** (warning
  border), **Senior tip** (success border). Use a small inline SVG icon,
  not an emoji.
- **Figures**: numbered `Figure {part}.{n}`, caption below in muted text.
  `break-inside: avoid`.

## 3. Visualization & equation rendering — strict

- Every figure is a real visual: a **Mermaid** diagram or **inline SVG**.
- **No ASCII art, no box-drawing diagrams, no text-based figures.**
- SVGs are hand-written, with `viewBox` and labelled `<text>` elements;
  any text inside an SVG is at least 12 px.
- All figures have explicit captions placed below them.

### Mermaid configuration & legibility — non-negotiable

The printed page content area is ~174 mm wide. A flowchart with more
than five nodes laid out left-to-right becomes unreadable when scaled
to that width. Apply every rule below.

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
  appears as 3-5 subgraphs stacked top-to-bottom.
- **Node labels stay short — at most about 3 words.** Detail belongs in
  the figure caption.
- For **sequence diagrams**: at most ~5 participants and ~12 messages.
- For **mind-maps and graphs**: prefer `flowchart TB` with subgraphs
  over the raw `graph` syntax.
- After drafting each diagram, mentally render it at ~174 mm wide and
  ask *"would labels stay readable in print?"* If text would drop
  below ~12 px effective size, redesign before shipping.
- Always validate Mermaid syntax (matching brackets, correct directives
  like `flowchart TB`, `sequenceDiagram`, `mindmap`).
- **Figure height cap for print**: add the following CSS so that no
  single diagram overflows the page when printed:
  ```css
  .mermaid svg { max-width: 100% !important; max-height: 650px; height: auto !important; }
  ```

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

- **MathJax typeset guard** — add a script at the end of `<body>` that
  forces MathJax to finish rendering before the user can print. This
  prevents raw LaTeX from appearing in the PDF:

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
- **Display math goes in its own block.** Wrap each display equation in
  `<div class="math-display">$$ ... $$</div>` styled with
  `text-align: center`, 12 pt top and bottom margin, and
  `break-inside: avoid; page-break-inside: avoid`.
- **Heading + equation grouping**: when a `<h2>` or `<h3>` is
  immediately followed by a short paragraph and a display equation,
  wrap all three in a `<div style="break-inside: avoid;
  page-break-inside: avoid;">` so the heading never lands at the
  bottom of a page with the equation orphaned on the next.
- **Never put math inside `<code>` or `<pre>`**, and never inside a
  markdown fenced code block. MathJax skips those tags, so the source
  renders literally.
- After drafting, scan every formula visually: it must appear as
  typeset math, never as raw `\(...\)` or `$$...$$` source.

**Figures required in this volume:**

| #  | Figure                                                                  | Type                | Part |
|----|-------------------------------------------------------------------------|---------------------|------|
| 11 | Inference stack: request → router → engine → KV cache                   | Mermaid graph       | 6    |
| 12 | Quantization formats compared (bits / quality / VRAM trade-offs)        | Inline SVG bar chart| 6    |
| 13 | Streaming + caching request lifecycle                                   | Mermaid sequence    | 7    |
| 14 | Evaluation taxonomy (offline / online / human / LLM-judge)              | Mermaid mindmap     | 8    |
| 15 | RAG evaluation metrics map (RAGAs)                                      | Mermaid graph       | 8    |
| 16 | LLM threat-model overview                                               | Mermaid flow        | 9    |
| 17 | LLMOps lifecycle wheel (CI / CD / CT + monitoring)                      | Inline SVG circular | 10   |

**Specific layout requirements for individual figures**

- **Figure 11** (inference stack) — `flowchart TB` with stage subgraphs
  stacked vertically: request handling → routing → engine → KV cache.
  Each subgraph contains at most 3 nodes.
- **Figure 16** (LLM threat-model overview) — `flowchart TB`. Group by
  attack class (input-side / tool-side / output-side) using subgraphs.

## 4. Content — what each Part must contain

### Part 6 — Inference optimization & serving *(~6 pages)*
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

### Part 7 — Production engineering for LLM apps *(~5 pages)*
- Streaming over SSE / WebSockets, backpressure, cancellation tokens.
- Caching: exact-match, semantic cache, provider-side prompt caching
  (Anthropic / OpenAI prompt-cache features).
- Multi-provider routing: LiteLLM, OpenRouter, Portkey. Failover and
  cost-aware routing.
- Structured outputs: JSON-mode, tool-call constraints, libraries like
  Outlines, Instructor, Guidance.
- Reliability: retries with exponential back-off and jitter, idempotency,
  circuit breakers, rate-limit handling.
- Token budgeting: conversation windowing, summarization compression,
  sliding windows.
- Include **Figure 13**.
- Include a **15-line code snippet**: streamed FastAPI endpoint that
  proxies to an LLM provider with retry-with-jitter.

### Part 8 — Evaluation *(~5 pages)*
- Standard benchmarks and what they actually measure: MMLU, MMLU-Pro,
  BBH, GPQA, HumanEval, MBPP, MATH, IFEval. Caveats and contamination;
  contamination-resistant benchmarks (LiveBench, fresh QA sets).
- Human preference at scale: LMSYS Chatbot Arena and the limits of
  Elo-style preference rankings.
- Designing task-specific evals: golden sets, regression suites, sliced
  metrics, statistical significance and power.
- Synthetic eval generation: using an LLM to produce eval inputs and
  oracle answers, with the obvious circularity caveats.
- LLM-as-judge: pairwise, single-grade, G-Eval, MT-Bench. Bias and
  calibration. Position bias, length bias, self-preference bias.
- RAG evaluation: faithfulness, answer relevance, context precision /
  recall. RAGAs, TruLens, Phoenix.
- Agent evaluation: trajectory eval, tool-call accuracy, end-to-end
  success.
- Online evaluation: shadow traffic, A/B tests, win-rate, regret,
  user-feedback loops.
- Include **Figures 14 and 15**.
- Include a **15-line code snippet**: computing two RAGAs metrics on a
  sample dataset.

### Part 9 — Safety, security, responsible AI *(~4 pages)*
- Threat model: direct and indirect prompt injection, jailbreaks, data
  exfiltration, tool abuse, model supply-chain attacks.
- Defenses: input and output guardrails, NeMo Guardrails, Guardrails AI,
  Llama Guard, Prompt Guard, Rebuff.
- PII detection and redaction; content policy; the OWASP LLM Top 10.
- Bias, toxicity, fairness; provenance and citation enforcement;
  basic watermarking ideas.
- Compliance touch-points: GDPR, HIPAA, SOC 2 — LLM-specific data-handling
  pitfalls (training data, logging of prompts and completions, retention).
- Governance artifacts: model cards, system cards, dataset cards;
  NIST AI Risk Management Framework; EU AI Act obligations for general-
  purpose AI and high-risk applications (engineer-level awareness, not
  legal advice).
- Include **Figure 16**.

### Part 10 — MLOps & LLMOps *(~6 pages)*
- ML lifecycle: continuous integration, continuous delivery, continuous
  training (CT).
- Experiment tracking: MLflow, Weights & Biases, Comet, Neptune.
- Model registry and versioning; semantic versioning of models;
  signatures.
- Feature stores: Feast, Tecton, Hopsworks — and where they fit (or
  honestly do not fit) for LLM workflows.
- Pipeline orchestration: Airflow, Kubeflow Pipelines, Metaflow, Flyte,
  Prefect, Dagster, ZenML.
- Data versioning: DVC, lakeFS, Delta Lake.
- Containerization and orchestration: Docker, Kubernetes, KServe,
  Knative.
- Cloud ML platforms: AWS SageMaker, GCP Vertex AI, Azure ML, Databricks.
- Monitoring and drift: Evidently, WhyLabs, Arize, Fiddler. Input drift,
  output drift, embedding drift, hallucination rate.
- LLMOps specifics:
  - Prompt registry and versioning.
  - Eval harness in CI (block PRs on regression).
  - LLM gateway pattern.
  - Feedback collection pipeline; the dataset flywheel.
  - Token-level FinOps: per-tenant / per-feature cost attribution,
    showback, budget alerts, fallback to cheaper models on cost spikes.
  - Multi-region deployment, blue-green / canary for models, rollback
    strategy when a new model version regresses silently.
- Observability: LangSmith, LangFuse, Helicone, OpenLLMetry, the
  OpenTelemetry GenAI semantic conventions.
- Include **Figure 17**.
- Include a **15-line YAML snippet**: GitHub Actions workflow that runs
  an eval-harness on PRs and fails on regression.

## 5. Code-snippet rules

- Each snippet stays between **10 and 30 lines**.
- Must be valid, runnable as written, using up-to-date APIs.
- No boilerplate scaffolding — only the conceptually important code.
- One-line caption above each snippet.
- Use Prism.js classes (`<pre><code class="language-python">…`).

## 6. Hard constraints

1. **One self-contained HTML artifact** for this volume. Inline CSS. CDN
   scripts only for Mermaid, Prism.js, optional MathJax.
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
   Honor `widows: 2; orphans: 2`.
8. **Density discipline**: dense, information-rich prose. No filler.
9. **HTML root must carry `lang="en"`** so hyphenation engages.
10. **Every Part must open with a one-sentence italic deck line** under
    its title.
11. **This is Volume 2 of 3**. Render only Parts 6-10 in this artifact.
    Do not generate content for Parts 1-5 or 11-15.

## 7. Self-review pass before delivery

Before returning the artifact:

1. Re-read the document end-to-end.
2. Validate every Mermaid diagram: matching brackets; correct directives
   (`flowchart TB`, `sequenceDiagram`, `mindmap`); no row longer than
   5 nodes; repeating structures shown as a single `subgraph` with
   `× N`, never unrolled. Confirm the `mermaid.initialize` block is
   present with `fontSize: '15px'`.
3. Confirm Figures 11-17 are present and correctly numbered (using the
   `Figure {part}.{n}` scheme — e.g., the first figure in Part 6 is
   `Figure 6.1`).
4. Confirm all required code snippets are present and within the line
   budget.
5. Sweep for grammar, spelling, agreement, consistent tense.
6. Sweep for any factual claim you are not confident about — soften or
   remove.
7. Sweep for any ASCII figure that may have slipped in.
8. Verify the print-CSS rules and page-break selectors.
9. Confirm no mention of interviews, hiring, recruitment, or personal
   names.
10. Confirm every Part has its mandatory italic deck line.
11. Confirm `<html lang="en">` is set.
12. Confirm MathJax 3 is loaded in `<head>` with the inline-math
    delimiter config block placed BEFORE the loader script. Visually
    verify each equation renders as typeset math, never as raw
    `\(...\)` or `$$...$$` source. No math inside `<code>` or `<pre>`.

Only then deliver.

---

**Begin now.** Output the complete Volume 2 HTML artifact.
