# Eval Atlas

A map of safety evaluations for robots and embodied AI: what they measure, which systems they test, and where the
gaps are. Each evaluation is tagged by domain, architecture and threat model, and scored for task complexity,
dexterity, cognition and relevance to catastrophic risk. A short list of gap findings sits on top of the data.

The atlas is a single static page, `docs/index.html`. Open it in a browser; it needs no server and no network.
To publish it, enable GitHub Pages for this repository with source `main` and folder `/docs`.

## Layout

- `db/entries/<id>.json`: one evaluation per file. Every field is required. Use `""` or `[]` when there is no value.
- `db/gaps/<id>.json`: one gap finding per file. `links` maps a name as written in `body` to an entry id or a URL.
- `db/vocab.json`: tag labels and scoring rubrics. Every tag in an entry must appear here. The page reads its labels from this file.
- `db/meta.json`: `updated` is the date shown on the page; `last_sweep` is where the next literature sweep starts.
- `db/removed/`: entries removed after review, kept as a record (see the inclusion rule below).
- `docs/index.html`: the page. Page copy and styling are edited here directly. The data block at the bottom is written by `atlas.py export`.
- `sources/abstracts.md`: arXiv abstracts used for facts. `python3 fetch_abstracts.py <id1,id2>` appends more.
- `factcheck-2026-11-03.md`: a full-text fact-check of all entries as of 3 Nov 2026. Its corrections are in `db/`.

## Tool

`atlas.py` needs only Python 3 and its standard library.

```
python3 atlas.py check     validate every entry and gap against db/vocab.json
python3 atlas.py stats     counts that the gap texts rely on
python3 atlas.py new <id>  write a blank entry to db/entries/<id>.json
python3 atlas.py fmt       rewrite all db files in the house layout (one field per line, so diffs are readable)
python3 atlas.py export    check, then embed the data in docs/index.html
```

## Periodic update

1. Search arXiv from `last_sweep` onwards. Add each new evaluation with `python3 atlas.py new <id>`, then fill in the file. Check fidelity, availability and code links against the full text, not the abstract.
2. Run `python3 atlas.py check` until it reports OK.
3. Run `python3 atlas.py stats` and compare it with the counts the gap texts state. Edit `db/gaps/` where they no longer hold.
4. Set `updated` and `last_sweep` in `db/meta.json`.
5. Run `python3 atlas.py export`, then open `docs/index.html` in a browser to check it.

## Inclusion rule

An entry measures safety-relevant behaviour or capability of a robot or embodied system, using a protocol someone
else could apply. Out of scope: mitigations and monitors as such, autonomous driving, pure capability or
robustness-only papers, and evaluations with no link to robotics (WMDP-Bio, VCT, LAB-Bench, MM-SafetyBench and
FigStep were removed for this reason).

Removed 3 Nov 2026, files in `db/removed/`: LabSafety Bench (no robot or agent acts), LabVLA (a model paper; its
measure is LabUtopia), L3-Bench (a protocol with no experiments), SimuGuard (audits the simulator, not a safety
behaviour; gap 5 still links the paper), Limits of Statistical Assurance (a certification-theory and monitoring
paper; its one robot experiment uses a scripted attacker, and the language-model results are on AgentDojo; gap 5
still links the paper). Kept after review: HASARD (embodied RL agents in game environments) and TRUST
(chain-of-thought monitoring axes for VLAs).

## Contributing

Corrections and additions are welcome.

- **Report a problem**: open an issue naming the entry id, the field you think is wrong, and the passage in the paper that shows it.
- **Propose a new evaluation**: check it against the inclusion rule above, then either open an issue with a link to the paper or send a pull request:
  1. `python3 atlas.py new <id>` (a short lowercase id, e.g. `safebench-x`) and fill in every field. Use labels from `db/vocab.json`, and give a one-line reason for each score in `why`.
  2. Take facts (fidelity, availability, code links, numbers) from the paper's full text, not the abstract.
  3. Run `python3 atlas.py fmt`, `python3 atlas.py check` (it must report OK) and `python3 atlas.py export`.
  4. In the pull request, say if the new entry changes a count that a gap text in `db/gaps/` relies on (`python3 atlas.py stats`).
- **Scores are judgements.** If you disagree with one, explain why with reference to the rubric in `db/vocab.json`. Disagreements are useful even when the score stays.
- **Changes to the page** (`docs/index.html`): keep it a single self-contained file with no external requests.

## How to cite

If you use the data or the analysis, please cite the atlas. GitHub shows a "Cite this repository" button from
`CITATION.cff`; the BibTeX equivalent is:

```bibtex
@misc{eval_atlas_2026,
  author       = {Alt, Benjamin},
  title        = {Eval Atlas: Mapping physical AI safety evaluations},
  year         = {2026},
  url          = {https://github.com/Convergent-Robotics/eval-atlas},
  note         = {Dataset and analysis, version of 9 November 2026}
}
```

When you cite a specific evaluation, please cite its original paper too; each entry's `url` points to it.

## License

- Code (`atlas.py`, `fetch_abstracts.py`, `docs/index.html`): MIT, see [`LICENSE`](LICENSE).
- Data and text (`db/`, the gap findings and the page copy, `factcheck-2026-11-03.md`): CC BY 4.0, see [`LICENSE-DATA`](LICENSE-DATA).

`sources/abstracts.md` quotes arXiv abstracts, which remain under their authors' licenses.
