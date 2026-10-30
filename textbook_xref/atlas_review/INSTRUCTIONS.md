# Atlas cross-reference: Anatomy-by-OR-case pages and OR cards (ENT Mastery v51)

This is for a Claude chat that can read the user's local PDFs (Claude desktop, linked to this computer). The cloud session cannot read these books: they are over 10 MB, and Drive returns no text.

## Books to use
- **Atlas of Head and Neck Surgery**, Simo, Pracy & Fernandes, 2024 ed. Drive: ENT Boards Library / "Atlas of Head and Neck Surgery.pdf".
- **Janfaza, Surgical Anatomy of the Head and Neck**, 1e. Drive: ENT Boards Library / "Surgical Anatomy of the Head and Neck ( PDFDrive ).pdf".
- **Optional for checking otology, sinus and skull-base items:** Atlas of Endoscopic Sinus and Skull Base Surgery, and the Cummings 7e parts.

## What to check
Each line in `atlas_xref_part1.md` through `atlas_xref_part6.md` is one claim, with an id such as `A-parotidectomy.landmark1` or `OR-parotidectomy.step3`. For every claim:
1. Find the passage in the books that covers it. Use the surgical atlas for operative steps and danger structures, and Janfaza for anatomic relationships, nerve courses, foramina and blood supply.
2. Give it a verdict:
   - **OK**: the book supports the claim.
   - **CORRECT**: the claim is wrong. Give the fix.
   - **CONFLICT**: the sources disagree. Give a suggested wording that covers both.
   - **UNSUPPORTED**: neither book covers the claim. Do not invent a citation.
3. Lines not covered by either book can be skipped. Focus on anatomy, landmarks, danger structures, variants, supply and pimp answers.

## Output
For each part, write a CSV named `corrections_atlas_partN.csv` (N = 1-6) with exactly these columns, matching the earlier textbook review:

```
item_id,verdict,quoted_claim,book,edition_chapter,printed_page,book_text_excerpt,suggested_fix
```

- `book` examples: "Simo, Pracy & Fernandes, Atlas of Head and Neck Surgery (2024)" or "Janfaza, Surgical Anatomy of the Head and Neck". Separate multiple books with " | ".
- `edition_chapter` examples: "2024 ed, Ch 46 Total Thyroidectomy..." or "1e, Ch 4 Neck".
- `printed_page` is the printed page number, not the PDF page.
- `book_text_excerpt` is a short verbatim excerpt (under about 40 words).

Upload each CSV to the **ENT Boards Library** Drive folder. The cloud session will pick them up, apply the corrections to the anatomy pages and OR cards, and add the page citations to each page's sources.
