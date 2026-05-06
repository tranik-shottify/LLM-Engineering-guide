# Prompt — Volume 1 of 5

Paste this entire message into a fresh claude.ai conversation. This is
**Volume 1 of a 5-volume reference document on LLM engineering**. Each
volume is rendered in its own conversation and produced as a separate,
standalone print-ready HTML artifact. Volumes share visual style so the
five PDFs look like one consistent series.

**This volume contains**: Cover page, abstract, "Volume contents", and
**Parts 1-3** — Foundations refresher, Modern model landscape, Adapting
models (SFT / PEFT / alignment / distributed training).

---

I want you to produce a **single, polished, print-ready HTML artifact**
titled **"LLM Engineering — A Practitioner's Reference · Volume 1"**.
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
- **Target length when printed: 22-26 A4 pages** for this volume.
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

  /* Figures: hard absolute cap on height so they always fit one page.
     Printable height at 20mm/22mm vertical margins on A4 ≈ 255mm.
     Cap at 200mm to leave room for caption + breathing space. */
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

> **Why these rules matter.** `break-inside: avoid` is only a hint to the
> browser; if an element is taller than the printable page area, the
> browser must break it anyway. The `!important` weight, the absolute-
> unit caps in mm, and the explicit `figure svg { max-height: 180mm }`
> rule together prevent Mermaid's inline SVG sizing from overriding the
> cap. Without these, a single Mermaid diagram routinely renders 700-
> 900 px tall and gets sliced across two pages even when the figure has
> `break-inside: avoid`.

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
  document title with " · Volume 1" on the right.
- **Page footer**: page number `counter(page) / counter(pages)` centered;
  small "Volume 1 of 5" on the left.
- **Cover page** (page 1, no header/footer):
  - Top third of the page is whitespace.
  - A short horizontal accent rule, ~40 % page width, 2 px solid `#0F2A4A`,
    sitting just above the title.
  - Title: **LLM Engineering — A Practitioner's Reference**, **44 pt**,
    weight 700, navy, balanced wrapping.
  - Subtitle directly below: *Volume 1 · Foundations · Models ·
    Adaptation*, **16 pt**, weight 400, muted color `#4A5568`.
  - A tasteful decorative SVG element in the lower portion of the page —
    a thin geometric band or angled stripes in `#0F2A4A` and `#1F6FEB`.
    Restrained, not loud.
  - Date line near the bottom: "2026 Edition", 11 pt, muted.
  - **No author, no logo, no personal details.**
- **Volume contents** (page 2): list of the three Parts in this volume only,
  with leader dots and page numbers. Add a small **"Companion volumes"**
  note listing — by name only, no page numbers — what
  - Volume 2 (Parts 4-6: Retrieval-Augmented Generation, Agentic systems,
    Inference optimization & serving)
  - Volume 3 (Parts 7-9: Production engineering, Evaluation, Safety &
    security)
  - Volume 4 (Parts 10-12: MLOps & LLMOps, Multimodal, System design
    playbook)
  - Volume 5 (Parts 13-15: Trends, Curated resources, Glossary)

  contain.

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
- **Callouts**: three styles — **Key idea** (blue left border `#1F6FEB`),
  **Pitfall** (warning border `#B45309`), **Senior tip** (success border
  `#1F8B4C`). Use a small inline SVG icon, not an emoji.
- **Figures**: numbered `Figure {part}.{n}`, caption below in muted text.
  `break-inside: avoid`.

## 2.5 "How to save as PDF" callout (visible on screen, hidden in print)

At the very top of the rendered HTML — directly after the cover but
before the volume opener — add a `<div class="no-print">` callout that
the user sees on screen but is hidden in print output. Style it the
same as a "Key idea" callout (soft `#F4F6FA` background, blue left
border) and place it inside `<div class="screen-only no-print">`.

The callout text:

> **How to save this volume as a PDF.** Open this file in **Chrome** or
> Edge. Wait until every diagram and equation has finished rendering on
> screen. Press **Ctrl+P / ⌘P**. Set destination to **"Save as PDF"**.
> Under "More settings": **Margins → Default** (let the document's
> `@page` rule control margins — do not pick "None" or "Custom"),
> **Paper size → A4**, **Scale → Default (100 %)**, and **enable
> "Background graphics"** so banners and callout fills render. Then
> click **Save**.

Add a `.screen-only { display: block; }` rule and rely on the
`@media print { .no-print { display: none !important; } }` rule
already in the print CSS to remove it from the printed output.

## 3. Visualization & equation rendering — strict

- Every figure is a real visual: a **Mermaid** diagram or **inline SVG**.
- **No ASCII art, no box-drawing diagrams, no text-based figures.** If you
  cannot produce a proper visual for a listed figure, omit it rather than
  fall back to ASCII.
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
  when a diagram has at most five nodes total. The page is portrait A4;
  vertical flows fit, long horizontal chains get crushed.
- **Never chain more than 5 nodes in a single row.** If a flow has more
  stages, switch direction or split into stacked subgraphs.
- **Do not unroll repeating structures.** For "× N decoder blocks" or
  any repeated stage, show one instance as a `subgraph` and mark
  multiplicity with a labeled loop-back edge or an explicit `× N`
  annotation on the subgraph border.
- **Use `subgraph` to group logically.** A pipeline with 3-5 stages
  appears as 3-5 subgraphs stacked top-to-bottom, each holding 2-4
  nodes — not one long unbroken chain. **Limit to four subgraphs**
  per figure; if a flow needs more, split into Figure N.a / N.b.
- **Node labels stay short — at most about 3 words.** Detail belongs in
  the figure caption, not crammed into boxes.
- For **sequence diagrams**: at most ~5 participants and ~12 messages
  per diagram. Split if longer.
- For **mind-maps and graphs**: prefer `flowchart TB` with subgraphs
  over the raw `graph` syntax — it renders larger and cleaner under
  print CSS.
- After drafting each diagram, mentally render it at ~174 mm wide and
  ask *"would labels stay readable in print, and would the diagram
  fit inside 180 mm of vertical space?"* If not, redesign — reduce
  nodes, switch to TB, or abstract the repeating segment.
- Always validate Mermaid syntax (matching brackets, no stray commas,
  correct directives like `flowchart TB`, `sequenceDiagram`, `mindmap`).
- The print CSS already caps `figure svg { max-height: 180mm !important }`,
  but Mermaid still renders at its natural size and will be scaled
  down — keep diagram complexity low so the scaled version is legible.

### Math rendering — non-negotiable

A previous draft rendered TeX source as literal text on the page —
expressions like `$\mathcal{L} = -\dfrac{1}{N}\sum ...$` appeared
uncompiled. That must not happen. Every equation must render as proper
math typography.

- **Include MathJax 3 in the document `<head>`**, with the delimiter
  config defined BEFORE the loader script. Use this exact pattern:

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

- **Render-completion guard** — add a script at the end of `<body>` that
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
  NOT use bare `$...$` for inline (it collides with currency strings
  like "$5" in prose).
- **Display math goes in its own block** with breathing room above and
  below. Wrap each display equation in
  `<div class="math-display">$$ ... $$</div>` styled with
  `text-align: center`, 12 pt top and bottom margin, and
  `break-inside: avoid; page-break-inside: avoid` so the equation
  never splits across pages.
- **Heading + equation grouping**: when a `<h2>` or `<h3>` is
  immediately followed by a short paragraph and a display equation,
  wrap all three in a `<div style="break-inside: avoid;
  page-break-inside: avoid;">` so the heading never lands at the
  bottom of a page with the equation orphaned on the next.
- **Never put math inside `<code>` or `<pre>`** — MathJax skips those
  tags by configuration, so `\(...\)` inside them renders as literal
  text.
- **Do not place math inside a markdown fenced code block.** Use plain
  HTML containers around the delimiters.
- After drafting, scan every formula visually: it must appear as
  typeset math, never as raw `\(...\)` or `$$...$$` source.

**Figures required in this volume:**

| #  | Figure                                                                  | Type              | Part |
|----|-------------------------------------------------------------------------|-------------------|------|
| 1  | Transformer block: token → embed → attention → FFN → logits             | Mermaid flow      | 1    |
| 2  | Attention variants compared: MHA / MQA / GQA / MLA                      | Inline SVG        | 1    |
| 3  | Modern model-family tree: open-weight vs frontier closed (2025-2026)    | Mermaid graph     | 2    |
| 4  | PEFT method comparison (LoRA / QLoRA / DoRA / AdaLoRA / IA³)            | Inline SVG figure | 3    |
| 5  | Alignment pipeline: pretrain → SFT → preference optimization            | Mermaid flow      | 3    |

**Specific layout requirements for individual figures**

- **Figure 1** (Transformer decoder block) — render as `flowchart TB`.
  The decoder block is one `subgraph` with internal nodes (pre-norm →
  self-attention → residual → pre-norm → FFN → residual). Annotate the
  subgraph border with `× N` to indicate repetition. Do **not** unroll
  the loop into a horizontal chain.
- **Figure 3** (model-family tree) — `flowchart TB`. One subgraph per
  category (open-weight, frontier closed, reasoning, SLMs). Each
  subgraph holds 2-4 representative model names; do not list every
  variant. Cap at four subgraphs total.
- **Figure 5** (alignment pipeline) — `flowchart TB`. Three or four
  stage nodes stacked vertically (pretrain → SFT → preference
  optimization → optional safety / RLAIF), with short labels on each
  edge.

## 4. Content — what each Part must contain

### Part 1 — Foundations refresher *(brief but complete, ~7-8 pages)*
- Transformer architecture: encoder, decoder, decoder-only.
- Attention math: scaled dot-product `softmax(QKᵀ/√d)V`; variants MHA, MQA,
  GQA, MLA — when each is used and why (memory-bandwidth, KV-cache size).
- Modern decoder-block components: pre-norm vs post-norm, RMSNorm vs
  LayerNorm, SwiGLU / GeGLU, residual paths — why contemporary open-weight
  LLMs all look broadly similar.
- Tokenization: BPE, SentencePiece, tiktoken; vocabulary size, byte-level
  fall-back, multilingual coverage and token-economics implications.
- Special tokens and chat templates: BOS / EOS / PAD, system / user /
  assistant roles, ChatML, the Llama 3 chat template, why the wrong
  template silently degrades quality.
- Positional encodings: absolute, RoPE, ALiBi, YaRN, NTK-aware scaling.
- Logits, softmax, cross-entropy loss, perplexity — show the cross-entropy
  formula and the perplexity ↔ loss relationship.
- Training objectives: causal LM, MLM, span-corruption.
- Sampling and decoding strategies: greedy, beam search, temperature,
  top-k, top-p (nucleus), min-p, typical sampling, repetition / frequency /
  presence penalty, contrastive decoding. Practical guidance on which knob
  to turn for which symptom.
- Scaling laws: Kaplan and Chinchilla compute-optimal token-to-parameter
  ratio.
- In-context learning & prompt-engineering primitives: zero-shot,
  few-shot, chain-of-thought, system / user / assistant role-message
  structure, prompt templates and parameterization. Brief, not a tutorial.
- Embeddings: bi-encoders vs cross-encoders, dimensionality, similarity
  measures (cosine / dot / Euclidean).
- Context window vs *effective* context (lost-in-the-middle).
- Include **Figure 1 and Figure 2**.

### Part 2 — Modern model landscape (2025-2026) *(~4 pages)*
- Open-weight families currently in use: Llama 3.x and 4, Qwen 2.5 / 3,
  Mistral, Mixtral, Gemma 3, Phi-4, DeepSeek V3 and R1, Command-R / R+.
- Frontier closed: GPT-5 family, Claude 4.x (Opus / Sonnet / Haiku),
  Gemini 2.5.
- Reasoning models / test-time compute: o1, o3, DeepSeek-R1, QwQ — what
  they are, when their cost is justified.
- Architectures: dense Transformers, Mixture-of-Experts, State-Space Models
  (Mamba, Mamba-2), hybrids, early diffusion language models.
- Small Language Models and on-device: Phi, Gemma-nano, Llama 3.2 1B / 3B.
- Include **Figure 3**.

> **Accuracy note**: For any specific benchmark number, parameter count, or
> release date you are not confident about, either describe qualitatively
> ("a few hundred billion parameters", "released in 2025") or omit the
> figure. Do not invent benchmark scores or product names.

### Part 3 — Adapting models: SFT, PEFT, alignment, distributed training *(~10-12 pages)*
- When to use continued pre-training (DAPT) vs SFT vs preference
  optimization.
- Loss masking during SFT: training on completion tokens only, why
  template-bound masking matters, what goes wrong when you forget.
- PEFT family: LoRA, QLoRA, DoRA, AdaLoRA, LoftQ, IA³, prompt tuning,
  prefix tuning. Trade-offs: trainable parameters, VRAM, quality.
- Alignment: RLHF (PPO), DPO, IPO, KTO, ORPO, SimPO, RLAIF, Constitutional
  AI. Show the DPO loss in math.
- Synthetic data pipelines: distillation, self-instruct, evol-instruct,
  self-rewarding models.
- Distributed-training primer: DDP, FSDP, ZeRO stages 1 / 2 / 3, tensor
  parallel, pipeline parallel, sequence parallel — what each shards and
  when you need it. Mixed precision (bf16 vs fp16), gradient accumulation,
  gradient checkpointing, activation offloading.
- Model merging: TIES, DARE, SLERP, task-vector arithmetic, MergeKit.
- Practical fine-tuning tooling: TRL, Axolotl, Unsloth, LLaMA-Factory,
  Hugging Face `peft` and `accelerate`.
- Failure modes: catastrophic forgetting, reward hacking, alignment tax,
  mode collapse.
- Include **Figure 4 and Figure 5**.
- Include a **15-20 line code snippet**: minimal LoRA + SFT setup with
  HuggingFace `peft` and `trl` (`SFTTrainer`).

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
   or any role-related framing.** This is a learning reference document.
6. **No personal names, no logos, no company branding** beyond well-known
   public product names referenced for technical accuracy.
7. **Page-break discipline**: every Part starts on a new page; figures,
   code blocks, tables, and callouts must never be split across pages.
   Honor `widows: 2; orphans: 2`. Apply the print-CSS block in Section 2
   exactly as written, including all `!important` weights and absolute-
   unit caps.
8. **Density discipline**: dense, information-rich prose. No filler,
   no "in this section we will discuss…" preambles, no marketing language.
9. **HTML root must carry `lang="en"`** so hyphenation engages.
10. **Every Part must open with a one-sentence italic deck line** under
    its title.
11. **This is Volume 1 of 5**. Render only Parts 1-3 in this artifact.
    Do not generate content for Parts 4-15.

## 7. Self-review pass before delivery

Before returning the artifact:

1. Re-read the document end-to-end.
2. Validate every Mermaid diagram: matching brackets; correct directives
   (`flowchart TB`, `sequenceDiagram`, `mindmap`); no row longer than
   5 nodes; at most 4 subgraphs per figure; repeating structures shown
   as a single `subgraph` with `× N`, never unrolled. Confirm the
   `mermaid.initialize` block is present with `fontSize: '15px'`.
3. Confirm Figures 1-5 are present and correctly numbered using the
   `Figure {part}.{n}` scheme (e.g., the first figure in Part 1 is
   `Figure 1.1`).
4. Confirm all required code snippets are present and within the line
   budget. Confirm no math inside any `<pre>`/`<code>`.
5. Sweep for grammar, spelling, agreement, consistent tense.
6. Sweep for any factual claim you are not confident about — soften or
   remove.
7. Sweep for any ASCII figure that may have slipped in.
8. **Print-CSS verification**: confirm the `@media print` block contains
   the `!important` weight on every break/size rule, the figure
   `max-height: 200mm`, the `figure svg { max-height: 180mm !important }`
   rule, the `pre { max-height: 180mm; white-space: pre-wrap }`, the
   `thead { display: table-header-group }` rule, and the
   `tr { break-inside: avoid !important }` rule. These are what prevent
   images and code blocks from being sliced across pages in the
   exported PDF.
9. Confirm no mention of interviews, hiring, recruitment, or personal
   names.
10. Confirm every Part has its mandatory italic deck line.
11. Confirm `<html lang="en">` is set.
12. Confirm MathJax 3 is loaded in `<head>` with the inline-math
    delimiter config block placed BEFORE the loader script. Visually
    verify each equation renders as typeset math, never as raw
    `\(...\)` or `$$...$$` source. No math inside `<code>` or `<pre>`.
13. Confirm the screen-only "How to save as PDF" callout is present
    near the top, wrapped in `<div class="no-print">`, with the
    `.no-print { display: none !important }` rule active in the
    `@media print` block.

Only then deliver.

---

**Begin now.** Output the complete Volume 1 HTML artifact.
