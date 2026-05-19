# Att beskriva verksamheten rätt

En praktisk handbok/lärobok av Erland Lindmark om att identifiera och beskriva förmågor, processer, rutiner och närliggande verksamhetsbeskrivningar.

## Projektstruktur

- `chapters/` innehåller manuskapitel.
- `docs/` innehåller bokspecifikation, kapitelplan, projektstatus, terminologi och exportmetadata.
- `assets/cover/` är avsedd för omslagsbild.
- `assets/image-prompts/` innehåller promptar för omslag och eventuella framtida illustrationer.
- `styles/` innehåller CSS för EPUB/PDF.
- `scripts/` innehåller lokal exportpipeline.
- `exports/` är målplats för genererade EPUB/PDF/DOCX/Markdown-filer.

## Export

Kör lokalt från projektroten:

```bash
bash scripts/export-book.sh
```

Scriptet kräver Python 3 och rekommenderar Pandoc för EPUB/PDF-export.
