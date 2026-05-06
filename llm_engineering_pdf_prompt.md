# Prompt — paste this entire message into a fresh claude.ai conversation

---

I want you to produce a **single, polished, print-ready HTML artifact** titled
**"LLM Engineering — A Practitioner's Reference"**. I will save it as a PDF from
my browser, so the document must be styled for print. Treat this as a serious
technical reference document — comparable to a textbook chapter or a curated
engineering handbook — for a working machine-learning practitioner who already
ships LLM-powered software and now wants a comprehensive reference covering
modern, advanced, and 2025-2026-era LLM engineering and MLOps.

This is **not** a tutorial for beginners and **not** a marketing document.
It is a dense, accurate, well-organized engineering reference.

---

## 1. Output format (read carefully)

- Deliver **one HTML artifact**, fully self-contained except for these CDN scripts:
  - Mermaid (`https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js`)
  - Prism.js core + autoloader for syntax highlighting
  - Optionally MathJax for any math
- The HTML must include all CSS inline in a `<style>` block. No external CSS files.
- Target output when printed: **60-80 A4 pages**.
- The document must render correctly when I open the HTML file in Chrome and
  use "Print → Save as PDF". Page breaks, headers, footers, and figure
  placement must all behave under print CSS.
- If the artifact size limit forces you to split delivery across turns, do so,
  but always end each turn with a clear "continue with: <next-section>" pointer
  so I can ask you to proceed. Final delivery must be the full single HTML.

## 2. Page, typography, and color specification

Apply this exactly:

```css
@page { size: A4; margin: 18mm; }
@media print {
  .part { break-before: page; }
  figure, pre, .callout, table { break-inside: avoid; }
  h1, h2, h3 { break-after: avoid; }
}
```

- **Body font**: `Inter, "Segoe UI", system-ui, -apple-system, sans-serif`,
  11 pt, line-height 1.55, color `#1A1A1A` on `#FFFFFF`.
- **Headings**: same family, weights 600-700, generous top spacing.
  - H1 (Part title): 28 pt, color `#0F2A4A`.
  - H2 (Section): 18 pt, color `#0F2A4A`.
  - H3 (Subsection): 13 pt, color `#1F6FEB`.
- **Code**: `"JetBrains Mono", "Fira Code", Consolas, monospace`, 10 pt,
  background `#F4F6FA`, padding 12 px, border-radius 6 px, language label
  in top-right corner.
- **Color palette** (restrained, print-friendly):
  - Primary: `#0F2A4A` (deep navy)
  - Accent: `#1F6FEB` (blue)
  - Soft background for callouts: `#F4F6FA`
  - Success: `#1F8B4C`
  - Warning: `#B45309`
  - Muted text: `#4A5568`
- **Page header (running)**: small, muted, current Part name on the left,
  document title on the right.
- **Page footer**: page number `counter(page) / counter(pages)` centered,
  document title small on the left.
- **Cover page** (page 1, no header/footer):
  - Title: **LLM Engineering — A Practitioner's Reference**
  - Subtitle: *Architectures · Retrieval · Agents · Inference · Evaluation · LLMOps · 2025-2026*
  - A subtle decorative SVG band in `#0F2A4A`.
  - Date line: just the year, "2026 Edition".
  - **No author, no logo, no personal details.**
- **Table of contents** (page 2-3): auto-numbered with leader dots and page
  numbers; section titles linked.
- **Section openers**: each Part begins on a new page with a full-width tinted
  banner (`#F4F6FA` background, `#0F2A4A` text) containing "PART N" and the
  Part title.
- **Tables**: zebra striping (`#FAFBFD` alternate rows), no vertical lines,
  header row with `#0F2A4A` background and white text.
- **Callouts**: three styles — **Key idea** (blue left border `#1F6FEB`),
  **Pitfall** (warning border `#B45309`), **Senior tip** (success border
  `#1F8B4C`). Use a small inline SVG icon, not an emoji.
- **Figures**: numbered as `Figure {part}.{n}`, with caption below in muted
  text. `break-inside: avoid`.

## 3. Visualization rules — **strict**

- Every figure must be a real visual: a **Mermaid** diagram or **inline SVG**.
- **Do not produce ASCII art, box-drawing diagrams, or text-based figures
  under any circumstances.** If you cannot produce a proper visual for a
  given figure, omit that figure rather than fall back to ASCII.
- Mermaid diagrams should use the document's color palette where possible
  (set `themeVariables` via `mermaid.initialize({ theme: 'base', ... })`).
- SVGs should be hand-written and clean (viewBox set, labelled with `<text>`).
- All figures need an explicit caption.

The 20 figures the document must contain (place each in the indicated Part):

| #  | Figure                                                                        | Type             | Part |
|----|-------------------------------------------------------------------------------|------------------|------|
| 1  | Transformer block: token → embed → attention → FFN → logits                   | Mermaid flow     | 1    |
| 2  | Attention variants compared: MHA / MQA / GQA / MLA                            | Inline SVG       | 1    |
| 3  | Modern model-family tree: open-weight vs frontier closed (2025-2026)          | Mermaid graph    | 2    |
| 4  | PEFT method comparison (LoRA / QLoRA / DoRA / AdaLoRA / IA³)                  | Inline SVG table-figure | 3 |
| 5  | Alignment pipeline: pretrain → SFT → preference optimization (DPO/ORPO/RLHF)  | Mermaid flow     | 3    |
| 6  | Naive RAG vs Advanced RAG, side-by-side                                       | Mermaid flow     | 4    |
| 7  | GraphRAG / RAPTOR architecture                                                | Mermaid graph    | 4    |
| 8  | ReAct reasoning loop                                                          | Mermaid sequence | 5    |
| 9  | Multi-agent state graph (LangGraph-style)                                     | Mermaid graph    | 5    |
| 10 | Model Context Protocol: client ↔ server message flow                          | Mermaid sequence | 5    |
| 11 | Inference stack: request → router → engine → KV cache                         | Mermaid graph    | 6    |
| 12 | Quantization formats compared (bits / quality / VRAM trade-offs)              | Inline SVG bar chart | 6 |
| 13 | Streaming + caching request lifecycle                                         | Mermaid sequence | 7    |
| 14 | Evaluation taxonomy (offline / online / human / LLM-judge)                    | Mermaid mindmap  | 8    |
| 15 | RAG evaluation metrics map (RAGAs)                                            | Mermaid graph    | 8    |
| 16 | LLM threat-model overview                                                     | Mermaid flow     | 9    |
| 17 | LLMOps lifecycle wheel (CI / CD / CT + monitoring)                            | Inline SVG circular | 10 |
| 18 | Reference production architecture for an LLM application                     | Mermaid graph    | 12   |
| 19 | Cost vs latency Pareto sketch for serving choices                             | Inline SVG scatter | 12 |
| 20 | Technology timeline: 2023 → 2026                                              | Inline SVG timeline | 13 |

## 4. Content — what each Part must contain

The document has **15 Parts plus cover/TOC**. Total ≈ 60-80 printed pages.
Calibrate depth: the early "foundations" Part is brief (it only fixes
vocabulary); the bulk of the document is on advanced material and modern
practice.

### Part 0 — Front matter
Cover page, abstract (≤150 words explaining the document's purpose and how to
read it), and the table of contents.

### Part 1 — Foundations refresher *(brief but complete, ~9 pages)*
- Transformer architecture: encoder, decoder, decoder-only.
- Attention math: scaled dot-product (with the `softmax(QKᵀ/√d)V` form);
  variants MHA, MQA, GQA, MLA — when each is used and why
  (memory-bandwidth, KV-cache size).
- **Modern decoder-block components**: pre-norm vs post-norm, RMSNorm vs
  LayerNorm, SwiGLU / GeGLU activations, residual paths — the reasons
  contemporary open-weight LLMs all look broadly similar.
- Tokenization: BPE, SentencePiece, tiktoken; vocabulary size, byte-level
  fall-back, multilingual coverage and token-economics implications.
- **Special tokens and chat templates**: BOS / EOS / PAD, system / user /
  assistant roles, ChatML, the Llama 3 chat template, why the wrong template
  silently degrades quality.
- Positional encodings: absolute, RoPE, ALiBi, YaRN, NTK-aware scaling.
- **Logits, softmax, cross-entropy loss, perplexity** — the math layer the
  rest of the document sits on. Show the cross-entropy formula and the
  perplexity ↔ loss relationship.
- Training objectives: causal LM, MLM, span-corruption.
- **Sampling and decoding strategies**: greedy, beam search, temperature,
  top-k, top-p (nucleus), min-p, typical sampling, repetition / frequency /
  presence penalty, contrastive decoding. Practical guidance on which knob
  to turn for which symptom.
- **Scaling laws**: Kaplan and Chinchilla (compute-optimal token-to-parameter
  ratio), what they imply when deciding model size vs training data.
- **In-context learning & prompt-engineering primitives**: zero-shot,
  few-shot, chain-of-thought, system / user / assistant role-message
  structure, prompt templates and parameterization. Brief, foundational —
  not a prompt-engineering tutorial.
- Embeddings: bi-encoders vs cross-encoders, dimensionality, similarity
  measures (cosine / dot / Euclidean).
- Context window vs *effective* context (lost-in-the-middle).
- Include **Figure 1 and Figure 2**.

### Part 2 — Modern model landscape (2025-2026)
- Open-weight families currently in use: Llama 3.x and 4, Qwen 2.5 / 3,
  Mistral, Mixtral, Gemma 3, Phi-4, DeepSeek V3 and R1, Command-R/R+.
- Frontier closed models: GPT-5 family, Claude 4.x (Opus / Sonnet / Haiku),
  Gemini 2.5.
- Reasoning models / test-time compute: o1, o3, DeepSeek-R1, QwQ — what they
  are, when their cost is justified.
- Architectures: dense Transformers, Mixture-of-Experts, State-Space Models
  (Mamba, Mamba-2), hybrids, early diffusion language models.
- Small Language Models and on-device: Phi, Gemma-nano, Llama 3.2 1B / 3B,
  Apple/Google on-device approaches.
- Include **Figure 3**.

> **Accuracy note**: For any specific benchmark number, parameter count, or
> release date you are not confident about, either describe qualitatively
> ("a few hundred billion parameters", "released in 2025") or omit the figure.
> Do not invent benchmark scores. Do not invent product names.

### Part 3 — Adapting models: SFT, PEFT, alignment, distributed training
- When to use continued pre-training (DAPT) vs SFT vs preference optimization.
- **Loss masking during SFT**: training on completion tokens only, why
  template-bound masking matters, and what goes wrong when you forget.
- PEFT family: LoRA, QLoRA, DoRA, AdaLoRA, LoftQ, IA³, prompt tuning,
  prefix tuning. Trade-offs: trainable parameters, VRAM, quality.
- Alignment methods: RLHF (PPO), DPO, IPO, KTO, ORPO, SimPO, RLAIF,
  Constitutional AI. Show the DPO loss in math.
- Synthetic data pipelines: distillation, self-instruct, evol-instruct,
  self-rewarding models.
- **Distributed training primer**: DDP, FSDP, ZeRO stages 1 / 2 / 3, tensor
  parallel, pipeline parallel, sequence parallel — what each shards and
  when you need it. Mixed precision (bf16 vs fp16), gradient accumulation,
  gradient checkpointing, activation offloading.
- **Model merging**: TIES, DARE, SLERP, task-vector arithmetic, MergeKit.
- **Practical fine-tuning tooling**: TRL, Axolotl, Unsloth, LLaMA-Factory,
  Hugging Face `peft` and `accelerate` — what each is good for.
- Failure modes: catastrophic forgetting, reward hacking, alignment tax,
  mode collapse.
- Include **Figure 4 and Figure 5**.
- Include a **15-line code snippet** showing a minimal LoRA + SFT setup with
  HuggingFace `peft` and `trl` (`SFTTrainer`).

### Part 4 — Retrieval-Augmented Generation, beyond v1
- Chunking strategies: fixed-size, recursive, semantic, late chunking,
  proposition-based.
- Hybrid retrieval (BM25 + dense), Reciprocal Rank Fusion.
- Reranking: cross-encoders, Cohere Rerank, ColBERT-v2.
- Query transformation: HyDE, multi-query, step-back prompting,
  sub-question decomposition.
- Advanced patterns: parent-document retrieval, **contextual retrieval**
  (Anthropic), GraphRAG, RAPTOR, Self-RAG, Corrective RAG, Agentic RAG.
- **ANN index families**: HNSW, IVF, IVF-PQ, ScaNN, FAISS internals;
  recall vs latency vs memory trade-offs; when exact search still wins.
- Vector database landscape: Pinecone, Weaviate, Qdrant, Milvus, pgvector,
  LanceDB. Selection criteria (scale, filtering, hybrid support, ops).
- **Multi-vector retrieval**: ColBERT-v2 late interaction; ColPali for
  visual-document retrieval (page images instead of OCR).
- **Metadata filtering, time-decay / freshness, access-control filters**
  applied at retrieval time.
- **Document parsing tooling**: Unstructured, LlamaParse, Docling, Marker —
  why parsing quality often dominates retrieval quality in practice.
- Embedding model selection (MTEB leaderboard considerations);
  domain fine-tuning of embeddings (contrastive, hard-negative mining).
- Include **Figure 6 and Figure 7**.
- Include a **20-line code snippet** showing a hybrid retrieval +
  cross-encoder rerank pipeline.

### Part 5 — Agentic systems
- Patterns: ReAct, Plan-and-Execute, Reflexion, Tree-of-Thoughts, debate,
  router-agents.
- Frameworks: LangGraph, LlamaIndex Workflows, AutoGen, CrewAI, OpenAI
  Agents SDK, PydanticAI, smolagents — strengths and where each fits.
- Tool use and function calling: JSON Schema, structured outputs, parallel
  tool calls, JSON-mode quirks.
- **Model Context Protocol (MCP)**: anatomy (clients, servers, transport),
  realistic use cases (filesystem, database, internal API access), security
  considerations.
- Memory systems: scratchpad, episodic memory, semantic memory, vector +
  graph memory, *context engineering*.
- **Tool retrieval at scale**: embedding tool descriptions and selecting
  the top-k tools when you have hundreds of them, instead of shoving all
  schemas into context.
- **Computer-use / browser-control agents**: Anthropic Computer Use,
  OpenAI Operator-style approaches, Playwright-driven loops; the unique
  failure modes (mis-clicks, drift, shoulder-surfing risk).
- **Agent sandboxing and security**: how prompt-injection defenses for
  agents differ from chat (the agent acts on the injection); least-privilege
  tool design, human-in-the-loop confirmations for destructive actions.
- Multi-agent orchestration: hierarchical, graph-based, blackboard.
- Evaluating agents: trajectory eval, tool-call accuracy, end-to-end success.
- Cost and latency budgets for agentic systems.
- Include **Figures 8, 9, 10**.
- Include a **20-line code snippet** for a small LangGraph state graph with
  two nodes and a conditional edge.
- Include a **15-line code snippet** for a minimal MCP server (Python).

### Part 6 — Inference optimization & serving
- Engines: vLLM, TGI, TensorRT-LLM, SGLang, LMDeploy, llama.cpp, MLX, Ollama.
  Use cases.
- Quantization formats: BitsAndBytes 4/8-bit, GPTQ, AWQ, GGUF (Q4_K_M, Q5,
  Q8), SmoothQuant, FP8. Quality vs VRAM trade-off.
- KV-cache techniques: paged attention, prefix caching, KV reuse.
- **Speculative-decoding family**: vanilla draft-and-verify, Medusa,
  EAGLE / EAGLE-2, lookahead decoding, assisted generation — when each
  pays off and when it does not.
- **Disaggregated prefill / decode serving**: separating compute-bound
  prefill from memory-bound decode for better utilization.
- Continuous batching, chunked prefill, FlashAttention 2 / 3.
- Distillation and pruning at a high level.
- Mixed-precision serving.
- Serving stacks: BentoML, Ray Serve, KServe, NVIDIA Triton, Modal, RunPod,
  Baseten.
- Capacity planning: tokens/sec, $/1M tokens, GPU sizing, throughput vs
  latency trade-offs.
- Include **Figures 11 and 12**.
- Include a **10-line shell snippet** showing a representative
  `vllm serve` command with quantization and tensor-parallel flags.

### Part 7 — Production engineering for LLM apps
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
- Include a **15-line code snippet** showing a streamed FastAPI endpoint
  that proxies to an LLM provider with retry-with-jitter.

### Part 8 — Evaluation
- Standard benchmarks and what they actually measure: MMLU, MMLU-Pro, BBH,
  GPQA, HumanEval, MBPP, MATH, IFEval. Caveats and **contamination**;
  contamination-resistant benchmarks (LiveBench, fresh QA sets).
- Human preference at scale: **LMSYS Chatbot Arena** and the limits of
  Elo-style preference rankings.
- Designing task-specific evals: golden sets, regression suites, sliced
  metrics, **statistical significance and power** (sample-size sanity, not
  just point estimates).
- **Synthetic eval generation**: using an LLM to produce eval inputs and
  oracle answers, with the obvious circularity caveats.
- LLM-as-judge: pairwise, single-grade, G-Eval, MT-Bench. Bias and
  calibration. Position bias, length bias, self-preference bias.
- RAG evaluation: faithfulness, answer relevance, context precision /
  recall. RAGAs, TruLens, Phoenix.
- Agent evaluation: trajectory eval, tool-call accuracy, end-to-end success.
- Online evaluation: shadow traffic, A/B tests, win-rate, regret,
  user-feedback loops.
- Include **Figures 14 and 15**.
- Include a **15-line code snippet** computing two RAGAs metrics on a
  sample dataset.

### Part 9 — Safety, security, responsible AI
- Threat model: direct and indirect prompt injection, jailbreaks, data
  exfiltration, tool abuse, model supply-chain attacks.
- Defenses: input and output guardrails, NeMo Guardrails, Guardrails AI,
  Llama Guard, Prompt Guard, Rebuff.
- PII detection and redaction; content policy; the OWASP LLM Top 10.
- Bias, toxicity, fairness; provenance and citation enforcement; basic
  watermarking ideas.
- Compliance touch-points: GDPR, HIPAA, SOC 2 — LLM-specific data-handling
  pitfalls (training data, logging of prompts and completions, retention).
- **Governance artifacts**: model cards, system cards, dataset cards;
  **NIST AI Risk Management Framework**; **EU AI Act** obligations for
  general-purpose AI and high-risk applications (at the engineer's level
  of awareness, not legal advice).
- Include **Figure 16**.

### Part 10 — MLOps & LLMOps
- ML lifecycle: continuous integration, continuous delivery, **continuous
  training (CT)**.
- Experiment tracking: MLflow, Weights & Biases, Comet, Neptune.
- Model registry and versioning: semantic versioning of models, signatures.
- Feature stores: Feast, Tecton, Hopsworks — and where they fit (or
  honestly do not fit) for LLM workflows.
- Pipeline orchestration: Airflow, Kubeflow Pipelines, Metaflow, Flyte,
  Prefect, Dagster, ZenML.
- Data versioning: DVC, lakeFS, Delta Lake.
- Containerization and orchestration: Docker, Kubernetes, KServe, Knative.
- Cloud ML platforms: AWS SageMaker, GCP Vertex AI, Azure ML, Databricks.
- Monitoring and drift: Evidently, WhyLabs, Arize, Fiddler. Input drift,
  output drift, embedding drift, hallucination rate.
- **LLMOps specifics**:
  - Prompt registry and versioning.
  - Eval harness in CI (block PRs on regression).
  - LLM gateway pattern.
  - Feedback collection pipeline; the dataset flywheel.
  - **Token-level FinOps**: per-tenant / per-feature cost attribution,
    showback, budget alerts, fallback to cheaper models on cost spikes.
  - **Multi-region deployment, blue-green / canary for models, rollback
    strategy** when a new model version regresses silently.
- Observability: LangSmith, LangFuse, Helicone, OpenLLMetry, the
  OpenTelemetry GenAI semantic conventions.
- Include **Figure 17**.
- Include a **15-line YAML snippet** of a GitHub Actions workflow that
  runs an eval-harness on PRs and fails on regression.

### Part 11 — Multimodal & beyond text
- Vision-language models: LLaVA, Qwen-VL, InternVL, GPT-4o-vision, Gemini,
  Claude vision. Common interface patterns.
- **Visual document retrieval**: ColPali and the "skip OCR, embed page
  images directly" pattern; when it beats traditional parsing pipelines.
- Speech: Whisper-v3, Voxtral, real-time speech-to-speech models;
  **speaker diarization** and audio embeddings.
- Document AI / structured extraction: layout-aware models, table parsing.
- Brief note on image and video generation as steps inside agent pipelines
  (when they are appropriate).

### Part 12 — System design playbook
- Reference architecture for a production LLM application: stateless API
  layer, retrieval tier, model gateway, eval / observability sidecar,
  feedback store.
- Multi-tenancy and isolation, per-tenant quotas, model-level quotas.
- Scaling LLM workloads: horizontal vs vertical, autoscaling on
  tokens/sec or queue depth.
- Cost modelling: $/request, cache-hit economics, hosted-API vs self-hosted
  break-even — show a small worked example.
- Include **Figures 18 and 19**.

### Part 13 — Trends to watch (2025-2026)
- Agentic AI graduating from demos to production.
- **Computer-use / browser-control agents** moving from research demos
  into shipped products.
- MCP and emerging open tool-protocol standards.
- Long context (1M+ tokens) and the retrieval-vs-context trade-off.
- Test-time compute / reasoning depth as a deployment knob.
- On-device and edge LLMs.
- Synthetic-data flywheels and self-improvement loops.
- **Hardware shifts**: NVIDIA Blackwell (B200 / B300), AMD MI300X,
  AWS Trainium2, dedicated inference accelerators (Groq, Cerebras), and
  what they imply for cost-per-token over the next two years.
- **AI compilers and inference compilers** (TVM-MLIR, OpenAI Triton,
  Mojo) as the layer everyone forgets exists until they need it.
- World models and multimodal generalists.
- Include **Figure 20**.

### Part 14 — Curated resources
- Foundational papers (with one-line summary each): *Attention Is All You
  Need*, *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*,
  *LoRA*, *QLoRA*, *DPO*, *Self-RAG*, *vLLM / PagedAttention*,
  *FlashAttention*, *MoE / Switch Transformer*, *Mamba*. Use neutral
  descriptive language; do not invent links.
- Books worth reading: *Designing Machine Learning Systems* (Chip Huyen),
  *Machine Learning Engineering* (Andriy Burkov), *Hands-On Large Language
  Models* (Alammar & Grootendorst).
- Practitioner blogs: Lilian Weng, Sebastian Raschka, Eugene Yan.
- Open-source repositories worth reading code for.

### Part 15 — Glossary
A clean two-column glossary of ~60 terms used in the document. One-line
plain-English definition for each. Sorted alphabetically.

## 5. Code-snippet rules

- Each snippet stays between **10 and 30 lines**.
- Must be valid, runnable as written (assume standard libraries installed),
  and use up-to-date APIs.
- Show only the conceptually important code — no boilerplate scaffolding.
- Each snippet has a one-line caption above it explaining its purpose.
- Use Prism.js classes (`<pre><code class="language-python">…`).

## 6. Hard constraints

1. **One self-contained HTML artifact.** Inline CSS. CDN scripts only for
   Mermaid, Prism.js, optional MathJax.
2. **No ASCII art. No box-drawing diagrams. No text-based figures.** If a
   figure cannot be drawn properly with Mermaid or SVG, omit it.
3. **Technical accuracy first.** When unsure of a benchmark number, parameter
   count, or release date, describe qualitatively or omit the number. Never
   fabricate citations, URLs, or arXiv IDs. Quote dates and version numbers
   only when confidently known.
4. **Consistent American English** throughout.
5. **No mention of interviews, hiring, jobs, candidates, CVs, recruitment,
   or any role-related framing.** This is a learning reference document.
6. **No personal names, no logos, no company branding** beyond well-known
   public product names referenced for technical accuracy (e.g. Llama, vLLM,
   LangGraph, RAGAs).
7. **Page-break discipline**: every Part starts on a new page; figures, code
   blocks, tables, and callouts must never be split across pages.
8. **Density discipline**: prose should be dense and information-rich.
   No filler sentences, no "in this section we will discuss…" preambles,
   no marketing language. Write like an experienced engineer respecting the
   reader's time.

## 7. Self-review pass before delivery

Before you return the artifact:

1. Re-read the document end-to-end.
2. Check every Mermaid diagram for valid syntax (matching brackets,
   no stray commas, correct directives like `flowchart LR`, `sequenceDiagram`,
   `mindmap`).
3. Confirm all 20 listed figures are present and correctly numbered.
4. Confirm all required code snippets are present and within the line budget.
5. Sweep for grammar, spelling, agreement, and consistent tense.
6. Sweep for any factual claim you are not confident about — soften or remove.
7. Sweep for any ASCII figure that may have slipped in — replace with proper
   visual or remove.
8. Verify the print-CSS rules and page-break selectors compile correctly.
9. Confirm no mention of interviews, hiring, recruitment, or personal names.

Only then deliver the final artifact.

---

**Begin now.** If the work has to span multiple turns due to artifact size,
deliver Parts 0-5 in turn one, Parts 6-10 in turn two, Parts 11-15 plus the
final consolidated artifact in turn three. Otherwise deliver everything as one
artifact in a single turn.
