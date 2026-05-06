# Prompt — Volume 4 of 5

Paste this entire message into a fresh claude.ai conversation. This is
**Volume 4 of a 5-volume reference document on LLM engineering**. Each
volume is rendered in its own conversation and produced as a separate,
standalone print-ready HTML artifact. Volumes share visual style so the
five PDFs look like one consistent series.

**This volume contains**: a brief volume opener and **Parts 10-12** —
MLOps & LLMOps, Multimodal & beyond text, System design playbook.

---

I want you to produce a **single, polished, print-ready HTML artifact**
titled **"LLM Engineering — A Practitioner's Reference · Volume 4"**.
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
- All CSS inline in a `<style>` block.
- **Target length when printed: 18-22 A4 pages** for this volume.
- Renders correctly when opened in Chrome and printed via "Print → Save
  as PDF".

## 2. Page, typography, color (identical across all five volumes)

```css
@page { size: A4; margin: 20mm 18mm 22mm 18mm; }
html { hyphens: auto; -webkit-hyphens: auto; }
*, *::before, *::after { box-sizing: border-box; }
body { text-align: left; }
p { margin: 0 0 8pt 0; }

@media print {
  .part { break-before: page !important; page-break-before: always !important; }

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

  pre {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
    max-height: 180mm;
    overflow: hidden;
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .callout, .math-display {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
  }

  table { break-inside: auto; }
  thead { display: table-header-group; }
  tfoot { display: table-footer-group; }
  tr, td, th {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
  }

  h1, h2, h3, h4 {
    break-after: avoid !important;
    page-break-after: avoid !important;
    text-wrap: balance;
  }

  .section-banner, .part-banner {
    break-after: avoid !important;
    page-break-after: avoid !important;
  }

  p, li, dd { widows: 2; orphans: 2; }

  .no-print { display: none !important; }
}
```

The `<html>` root element must carry the attribute `lang="en"`.

> **Why these rules matter.** `break-inside: avoid` is only a hint; if
> an element is taller than the printable page area the browser must
> break it. The `!important` weight, the absolute-unit caps in mm, and
> the `figure svg { max-height: 180mm }` rule together prevent
> Mermaid's inline SVG sizing from overriding the cap.

- **Body**: `Inter, "Segoe UI", system-ui, -apple-system, sans-serif`,
  **12 pt**, line-height 1.55.
- **Headings**:
  - H1 (Part title): **32 pt**, weight 700, color `#0F2A4A`,
    line-height 1.15, `text-wrap: balance`.
  - H2 (Section): **20 pt**, weight 600, color `#0F2A4A`,
    24 pt top, 8 pt bottom, thin `1px solid #E5E9EF` bottom border.
  - H3 (Subsection): **14 pt**, weight 600, color `#1F6FEB`.
- **Code**: `"JetBrains Mono", "Fira Code", Consolas, monospace`, **11 pt**,
  background `#F4F6FA`, padding 12 px, border-radius 6 px. Language
  label in the top-right corner.
- **Figure captions** and other **muted text**: **10.5 pt**, color
  `#4A5568`.
- **Table captions**: **10.5 pt**, color `#4A5568`, placed *above* the
  table, prefixed `Table {part}.{n} · `.
- **Footnotes**: small superscript markers; footnote text **9.5 pt** at
  the bottom of the page.
- **Running header / footer**: **9 pt**, color `#4A5568`.
- **Color palette**: Primary `#0F2A4A`, Accent `#1F6FEB`, Soft callout
  `#F4F6FA`, Success `#1F8B4C`, Warning `#B45309`, Muted `#4A5568`.
- **Page header (running)**: small, muted, current Part name on the left,
  document title with " · Volume 4" on the right.
- **Page footer**: page number `counter(page) / counter(pages)` centered;
  small "Volume 4 of 5" on the left.
- **Volume opener page (page 1, no header/footer)**:
  - Top third whitespace, accent rule above title.
  - Title: **LLM Engineering — A Practitioner's Reference**, **44 pt**,
    weight 700, navy.
  - Subtitle: *Volume 4 · LLMOps · Multimodal · System Design*,
    **16 pt**, weight 400, muted.
  - Tasteful decorative SVG element in the lower portion.
  - Date line near the bottom: "2026 Edition", 11 pt, muted.
- **Volume contents (page 2)**: list of the three Parts in this volume,
  with leader dots and page numbers. Add a small "Companion volumes"
  note listing — by name only — what
  - Volume 1 (Parts 1-3: Foundations, Modern Model Landscape, Adapting
    Models)
  - Volume 2 (Parts 4-6: Retrieval-Augmented Generation, Agentic
    Systems, Inference Optimization & Serving)
  - Volume 3 (Parts 7-9: Production Engineering, Evaluation, Safety &
    Security)
  - Volume 5 (Parts 13-15: Trends, Curated Resources, Glossary)

  contain.

- **Section openers**: full-width tinted banner (`#F4F6FA` background,
  `#0F2A4A` text, **3 px solid `#1F6FEB` left border**, 16 px vertical
  padding). Three lines: `PART N` accent-blue tracked → Part title H1
  → italic deck (12.5 pt muted).
- **Tables**: full-width; zebra striping; no vertical rules; header row
  navy / white. Caption above.
- **Callouts**: **Key idea**, **Pitfall**, **Senior tip** with distinct
  left border colors. Inline SVG icon, not emoji.
- **Figures**: numbered `Figure {part}.{n}`, caption below.

## 2.5 "How to save as PDF" callout (visible on screen, hidden in print)

At the very top of the rendered HTML — directly after the volume opener
— add a `<div class="no-print">` callout that the user sees on screen
but is hidden in print output. Style it the same as a "Key idea"
callout.

The callout text:

> **How to save this volume as a PDF.** Open this file in **Chrome** or
> Edge. Wait until every diagram has finished rendering on screen.
> Press **Ctrl+P / ⌘P**. Set destination to **"Save as PDF"**. Under
> "More settings": **Margins → Default**, **Paper size → A4**,
> **Scale → Default (100 %)**, and **enable "Background graphics"** so
> banners and callout fills render. Then click **Save**.

## 3. Visualization & equation rendering — strict

- Every figure is a real visual: a **Mermaid** diagram or **inline SVG**.
- **No ASCII art, no box-drawing diagrams, no text-based figures.**
- SVGs are hand-written, with `viewBox` and labelled `<text>` elements;
  any text inside an SVG is at least 12 px.

### Mermaid configuration & legibility — non-negotiable

- **Initialize Mermaid once** near the top of the document:

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
- **Never chain more than 5 nodes in a single row.**
- **Do not unroll repeating structures** — use one `subgraph` with `× N`.
- **Use `subgraph` to group logically.** Limit to four subgraphs per
  figure; if a flow needs more, split into N.a / N.b.
- **Node labels stay short — at most about 3 words.**
- For **sequence diagrams**: at most ~5 participants and ~12 messages.
- After drafting each diagram, mentally render it at ~174 mm wide and
  ask *"would labels stay readable in print, and would the diagram fit
  inside 180 mm of vertical space?"* If not, redesign.
- Always validate Mermaid syntax.

### Math rendering — non-negotiable

- **Include MathJax 3 in the document `<head>`** with the delimiter
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

- **Render-completion guard** at the end of `<body>`:

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

- **Use `\(...\)` for inline math and `$$...$$` for display math.**
- **Display math goes in its own block** wrapped in
  `<div class="math-display">$$ ... $$</div>`.
- **Heading + equation grouping**: wrap heading + paragraph + equation
  in a single `<div style="break-inside: avoid;
  page-break-inside: avoid;">`.
- **Never put math inside `<code>` or `<pre>`**.

**Figures required in this volume:**

| #  | Figure                                                                  | Type                | Part |
|----|-------------------------------------------------------------------------|---------------------|------|
| 17 | LLMOps lifecycle wheel (CI / CD / CT + monitoring)                      | Inline SVG circular | 10   |
| 18 | Reference production architecture for an LLM application                | Mermaid graph       | 12   |
| 19 | Cost vs latency Pareto sketch for serving choices                       | Inline SVG scatter  | 12   |

**Specific layout requirements for individual figures**

- **Figure 17** (LLMOps lifecycle wheel) — inline SVG circular diagram
  with at most 6 segments, each labeled with a stage name (data prep,
  experimentation, training, eval, deploy, monitor). Inner caption:
  "Continuous Training (CT) loop". Total SVG height ≤ 150 mm.
- **Figure 18** (reference production architecture) — `flowchart TB`
  with subgraph layers stacked vertically: API tier → model gateway →
  retrieval & engines → eval & observability sidecar → feedback store.
  Each subgraph holds 2-4 nodes. **Limit to four subgraphs**; if a
  fifth tier is essential, drop it from the figure and discuss in
  prose only.

## 4. Content — what each Part must contain

### Part 10 — MLOps & LLMOps *(~7-8 pages)*
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

### Part 11 — Multimodal & beyond text *(~4-5 pages)*
- Vision-language models: LLaVA, Qwen-VL, InternVL, GPT-4o-vision, Gemini,
  Claude vision. Common interface patterns.
- Visual document retrieval: ColPali and the "skip OCR, embed page images
  directly" pattern; when it beats traditional parsing pipelines.
- Speech: Whisper-v3, Voxtral, real-time speech-to-speech models;
  speaker diarization and audio embeddings.
- Document AI / structured extraction: layout-aware models, table parsing.
- Brief note on image and video generation as steps inside agent pipelines
  (when they are appropriate).

### Part 12 — System design playbook *(~6-7 pages)*
- Reference architecture for a production LLM application: stateless API
  layer, retrieval tier, model gateway, eval / observability sidecar,
  feedback store.
- Multi-tenancy and isolation, per-tenant quotas, model-level quotas.
- Scaling LLM workloads: horizontal vs vertical, autoscaling on tokens/sec
  or queue depth.
- Cost modelling: $/request, cache-hit economics, hosted-API vs self-hosted
  break-even — show a small worked example, ideally with a short table
  of inputs (price/1K tokens, average prompt length, average completion
  length, requests/sec) and the resulting monthly cost for two options.
- Include **Figures 18 and 19**.

## 5. Code-snippet rules

- Each snippet stays between **10 and 30 lines**.
- Must be valid, runnable as written, using up-to-date APIs.
- No boilerplate scaffolding — only the conceptually important code.
- One-line caption above each snippet.
- Use Prism.js classes (`<pre><code class="language-yaml">…`).
- **No math inside any code block.**

## 6. Hard constraints

1. **One self-contained HTML artifact** for this volume.
2. **No ASCII art, no box-drawing diagrams, no text-based figures.**
3. **Technical accuracy first.** Never fabricate citations, URLs, or
   arXiv IDs.
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
9. **HTML root must carry `lang="en"`**.
10. **Every Part must open with a one-sentence italic deck line**.
11. **This is Volume 4 of 5**. Render only Parts 10-12 in this artifact.
    Do not generate content for Parts 1-9 or 13-15.

## 7. Self-review pass before delivery

Before returning the artifact:

1. Re-read the document end-to-end.
2. Validate every Mermaid diagram: matching brackets; correct directives;
   no row longer than 5 nodes; at most 4 subgraphs per figure;
   repeating structures shown as a single `subgraph` with `× N`.
   Confirm `mermaid.initialize` is present with `fontSize: '15px'`.
3. Confirm Figures 17, 18, 19 are present and correctly numbered using
   `Figure {part}.{n}` (e.g., `Figure 10.1`, `Figure 12.1`,
   `Figure 12.2`).
4. Confirm all required code snippets are present and within the line
   budget.
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

**Begin now.** Output the complete Volume 4 HTML artifact.
