# Kapitel 1: Varför verksamhetsbeskrivningar blir svåra

## Varför detta kapitel finns

Verksamhetsbeskrivningar blir sällan svåra för att människor saknar vilja att förstå verksamheten. De blir svåra därför att olika personer försöker använda samma beskrivning till olika saker.

En verksamhetsarkitekt kan vilja förstå vilka förmågor organisationen behöver stärka. En IT-arkitekt kan vilja förstå vilka system som stödjer vilka delar av verksamheten. En verksamhetsutvecklare kan vilja se var handläggningstider, dubbelarbete eller otydliga ansvar uppstår. Alla tre kan prata om “processen”, “förmågan”, “flödet” eller “rutinen”, men mena olika saker.

Det här kapitlet ger en första gemensam grund. Vi börjar inte med notationer, ramverk eller verktyg. Vi börjar med varför beskrivningar blir otydliga, och hur du kan undvika det genom att först klargöra syfte, målgrupp och modellnivå.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara varför verksamhetsbeskrivningar ofta blandar ihop olika begrepp och detaljnivåer
- skilja mellan syftet med en beskrivning och själva beskrivningen
- identifiera vem som ska använda en beskrivning och vilka frågor den behöver besvara
- upptäcka vanliga tecken på att en modell försöker lösa för många uppgifter samtidigt
- formulera en enkel startpunkt för en användbar verksamhetsbeskrivning

## Innan vi börjar

I bokens inledning introducerades verksamhetsbeskrivning som en avsiktlig beskrivning av någon aspekt av verksamheten, framtagen för ett visst syfte. Det är viktigt att hålla fast vid ordet **avsiktlig**.

En karta över förmågor, en processmodell, en rutinbeskrivning, en tjänstekarta och en ansvarsmatris kan alla vara bra beskrivningar. Men de är bra på olika saker. En vanlig orsak till problem är att organisationen väljer beskrivningsform innan den har bestämt vad beskrivningen ska användas till.

I det återkommande caset följer vi Tullmyndigheten Atlantis, en fiktiv tullmyndighet. Den vill förbättra sin förmåga att förstå, styra och utveckla verksamheten. Exemplet är förenklat och ska inte tolkas som en beskrivning av någon faktisk myndighet.

## Huvudförklaring

### Problemet börjar ofta med ett ord

Många diskussioner om verksamhetsbeskrivningar börjar med ett till synes enkelt ord:

“Vi behöver beskriva processen.”

Det kan låta tydligt, men ordet process kan användas på flera sätt i samma organisation. Någon menar ett värdeflöde från behov till resultat. Någon annan menar en uppsättning aktiviteter i ett ärende. En tredje menar en rutin i ett system. En fjärde menar en organisatorisk ansvarskedja.

Samma sak händer med ord som förmåga, tjänst, flöde, rutin, funktion, ansvar och arbetssätt. Orden är inte problemet i sig. Problemet uppstår när de används utan att någon först klargör vilken fråga de ska hjälpa till att besvara.

Ett praktiskt första steg är därför att fråga:

- Vad behöver vi förstå?
- Vem behöver förstå det?
- Vilket beslut, vilken förändring eller vilken samordning ska beskrivningen stödja?
- Vilken nivå av detalj är tillräcklig?
- Vad ska beskrivningen inte försöka visa?

De frågorna är ofta viktigare än valet av ritverktyg eller notation.

### Syftet styr formen

En verksamhetsbeskrivning bör alltid ha ett tydligt syfte. Syftet avgör vad som ska tas med, vad som kan utelämnas och vilken nivå som är rimlig.

Om syftet är att prioritera strategiska utvecklingsområden kan en förmågekarta vara mer användbar än en detaljerad processmodell. Om syftet är att förstå handläggningstider och överlämningar kan en processbeskrivning vara mer relevant. Om syftet är att säkerställa enhetligt utförande i ett visst arbetsmoment kan en rutin eller instruktion vara rätt nivå.

Det betyder inte att en beskrivning bara får ha ett användningsområde. Men ju fler användningsområden den ska stödja, desto större risk att den blir för omfattande, för detaljerad eller för vag.

En bra tumregel är:

> En verksamhetsbeskrivning ska vara så detaljerad att den kan användas för sitt syfte, men inte så detaljerad att den blir svår att förstå, förvalta eller fatta beslut utifrån.

### Målgruppen påverkar språket

En modell är inte bara en teknisk artefakt. Den är också ett kommunikationsmedel. Därför behöver du veta vem modellen är till för.

En ledningsgrupp behöver ofta se helhet, prioriteringar och konsekvenser. En processägare behöver förstå ansvar, resultat och förbättringsområden. En lösningsarkitekt behöver se kopplingar till information, system och integrationer. En handläggare kan behöva en konkret rutin eller instruktion.

Samma verksamhet kan därför behöva flera beskrivningar på olika nivåer. Det är inte dubbelarbete om beskrivningarna fyller olika syften och hänger ihop på ett medvetet sätt.

Problemet uppstår när en och samma modell förväntas vara:

- strategisk översikt
- operativ processbeskrivning
- kravunderlag
- utbildningsmaterial
- kontrollista
- systemdokumentation
- ansvarsmatris

Då blir modellen ofta svår att läsa och ännu svårare att förvalta.

### Modellnivå är inte samma sak som kvalitet

En detaljerad beskrivning är inte automatiskt bättre än en översiktlig beskrivning. En översiktlig beskrivning är inte automatiskt mer strategisk eller mer mogen.

Kvalitet handlar om passform mellan syfte, målgrupp, innehåll och nivå.

I Tullmyndigheten Atlantis case kan en hög nivå vara:

“Hantera varuflöden över gräns.”

Det kan vara relevant i en förmågekarta eller strategisk översikt. Men det är för grovt om syftet är att beskriva hur ett visst kontrollärende handläggs.

En mer detaljerad nivå kan vara:

“Registrera kompletterande uppgifter i ärendet.”

Det kan vara relevant i en rutin eller instruktion. Men det är för detaljerat om syftet är att diskutera vilka verksamhetsförmågor som behöver stärkas de kommande tre åren.

Båda beskrivningarna kan alltså vara bra. De svarar bara på olika frågor.

### När nivåer blandas ihop

Ett vanligt misstag är att blanda flera nivåer i samma lista eller modell. Då hamnar exempelvis stora verksamhetsförmågor, processer, arbetsmoment och systemfunktioner bredvid varandra som om de vore samma typ av sak.

Exempel på en blandad lista:

- Riskbedöma varuflöden
- Ta emot deklaration
- Klicka på “Begär komplettering”
- Hantera kontrollärende
- Skicka brev till aktör
- Tullklarering
- Kontrollera dokument
- Ärendehanteringssystem

Listan är inte värdelös. Den innehåller många relevanta observationer. Men den är ännu inte en färdig verksamhetsbeskrivning. Den blandar sannolikt förmågor, processer, aktiviteter, rutiner, tjänster, informationshantering och systemstöd.

Ett bättre nästa steg är inte att omedelbart rita om listan. Det bättre nästa steget är att sortera utsagorna efter vilken typ av fråga de verkar svara på.

| Utsaga | Möjlig typ | Fråga den svarar på |
|---|---|---|
| Riskbedöma varuflöden | Förmåga | Vad behöver verksamheten kunna? |
| Ta emot deklaration | Processaktivitet eller processteg | Vad händer i arbetet över tid? |
| Klicka på “Begär komplettering” | Rutin- eller instruktionssteg | Hur gör användaren i praktiken? |
| Hantera kontrollärende | Process eller förmåga beroende på syfte | Är detta ett flöde eller något verksamheten behöver kunna? |
| Ärendehanteringssystem | Systemstöd | Vilket stöd används? |

Tabellen är inte slutgiltig. Poängen är att skapa en arbetshypotes. När utsagorna har sorterats blir det lättare att avgöra vilken beskrivning som faktiskt behövs.

## Exempel: samma situation, tre olika beskrivningar

Tullmyndigheten vill förbättra hur den hanterar ärenden där uppgifter saknas eller behöver förtydligas. Olika personer beskriver behovet på olika sätt.

En verksamhetsutvecklare säger:

> “Vi behöver få ordning på processen för kompletteringar.”

En IT-arkitekt säger:

> “Vi behöver förstå vilket systemstöd som berörs när uppgifter begärs in och kommer tillbaka.”

En verksamhetsarkitekt säger:

> “Vi behöver se vilken förmåga det här egentligen stärker och hur den hänger ihop med digital service.”

Alla tre kan ha rätt. Men de behöver troligen inte samma beskrivning.

### Om syftet är förbättring av arbetsflödet

Då behöver organisationen sannolikt en processbeskrivning. Den kan visa startpunkt, resultat, aktiviteter, överlämningar, väntetider, roller och vanliga variationer.

Exempel på frågor:

- När uppstår behovet av komplettering?
- Vem avgör att uppgifter saknas?
- Hur kommuniceras begäran?
- Vad händer om svaret inte kommer in?
- Var uppstår väntetid eller dubbelarbete?

### Om syftet är strategisk planering

Då kan en förmågebeskrivning vara mer relevant. Den kan visa vilka förmågor som behöver finnas och utvecklas, oavsett exakt processflöde.

Exempel på frågor:

- Vilken verksamhetsförmåga är det som behöver stärkas?
- Är det en del av ärendehantering, riskbedömning, aktörsdialog eller digital service?
- Hur viktig är förmågan för myndighetens uppdrag?
- Hur mogen är förmågan i dag?
- Vilka utvecklingsinitiativ påverkar förmågan?

### Om syftet är enhetligt utförande

Då kan en rutin eller instruktion vara rätt beskrivning. Den behöver vara tillräckligt konkret för att stödja likartat arbetssätt.

Exempel på frågor:

- Vilka steg ska handläggaren följa?
- Vilka fält ska fyllas i?
- Vilka malltexter ska användas?
- Vilka undantag finns?
- När ska ärendet eskaleras?

Det är alltså inte frågan “ska vi beskriva processen?” som är viktigast. Den viktigaste frågan är: **vilken användning ska beskrivningen stödja?**

## Vanliga misstag

- **Misstag: Att börja med ritverktyget.**
  - Varför det händer: Verktyg ger en känsla av framdrift och konkret resultat.
  - Hur du undviker det: Skriv först en kort syftesmening och tre frågor som beskrivningen ska besvara.

- **Misstag: Att använda ett begrepp som om alla menar samma sak.**
  - Varför det händer: Ord som process, förmåga och flöde känns etablerade.
  - Hur du undviker det: Be deltagarna ge exempel på vad de menar och sortera exemplen efter nivå och användning.

- **Misstag: Att göra en modell för alla målgrupper.**
  - Varför det händer: Det upplevs effektivt att samla allt på ett ställe.
  - Hur du undviker det: Bestäm primär målgrupp. Skapa hellre flera kopplade beskrivningar än en överlastad modell.

- **Misstag: Att likställa detaljrikedom med kvalitet.**
  - Varför det händer: Detaljer kan se seriösa och genomarbetade ut.
  - Hur du undviker det: Bedöm kvalitet utifrån om beskrivningen hjälper målgruppen att fatta beslut eller utföra arbete.

- **Misstag: Att blanda verksamhet, organisation och systemstöd.**
  - Varför det händer: I praktiken upplevs arbetet ofta genom organisatoriska enheter och IT-system.
  - Hur du undviker det: Markera om en utsaga handlar om vad verksamheten behöver kunna, hur arbetet går till, vem som ansvarar eller vilket system som används.

## Övningar

### Övning 1: Hitta syftet

Läs följande situation:

Tullmyndigheten ska modernisera en del av sin ärendehantering. I ett första möte säger deltagarna att de behöver “en bild av processen”. Under samtalet visar det sig att några vill prioritera utvecklingsinitiativ, några vill hitta flaskhalsar, några vill förbättra instruktionerna för handläggare och några vill förstå beroenden till befintliga system.

Svara på frågorna:

1. Vilka olika syften finns i situationen?
2. Vilka målgrupper verkar behöva använda resultatet?
3. Vilka beskrivningstyper kan behövas?
4. Vilken beskrivning bör tas fram först, och varför?
5. Vilka risker finns om gruppen försöker skapa en enda modell för allt?

### Övning 2: Sortera utsagor

Sortera följande utsagor i preliminära kategorier. Använd kategorierna förmåga, process, rutin/instruktion, roll/ansvar, information, systemstöd eller oklart.

| Utsaga | Din kategori | Kort motivering |
|---|---|---|
| Bedöma risk i inkommande varuflöden |  |  |
| Skicka kompletteringsbegäran |  |  |
| Handläggare |  |  |
| Deklarationsuppgift |  |  |
| Ärendehanteringssystem |  |  |
| Följa upp obesvarade kompletteringar varje fredag |  |  |
| Besluta om kontrollåtgärd |  |  |
| Aktörsdialog |  |  |

Jämför sedan dina kategorier med syftet. Några utsagor kan hamna i olika kategorier beroende på vad beskrivningen ska användas till.

### Övning 3: Skriv en syftesmening

Välj en verksamhetsbeskrivning du själv har arbetat med eller behöver ta fram. Skriv en syftesmening enligt denna struktur:

“Den här beskrivningen ska hjälpa [målgrupp] att [användning/beslut/arbete] genom att visa [innehåll] på [nivå].”

Exempel:

“Den här beskrivningen ska hjälpa förändringsledningen att prioritera utvecklingsinsatser genom att visa centrala verksamhetsförmågor och deras beroenden på övergripande nivå.”

## Snabb sammanfattning

- Verksamhetsbeskrivningar blir ofta svåra när syfte, målgrupp och modellnivå är oklara.
- Samma ord kan användas på olika sätt i samma organisation.
- En beskrivning bör bedömas utifrån hur väl den stödjer sitt användningsområde.
- Detaljer är bara värdefulla när de hjälper målgruppen att förstå, besluta eller agera.
- En blandad lista med utsagor är ofta en bra start, men behöver sorteras innan den blir en användbar modell.
- Det är bättre att skapa flera kopplade beskrivningar än en enda modell som försöker bära alla behov.

## Quiz/reflektionsfrågor

1. Varför är frågan “vad ska beskrivningen användas till?” viktigare än frågan “vilken notation ska vi använda?”
2. Ge ett exempel på när en förmågebeskrivning är mer lämplig än en processbeskrivning.
3. Ge ett exempel på när en rutin är mer lämplig än en processmodell.
4. Vad kan hända om system, organisation, process och förmåga blandas i samma modell utan tydlig struktur?
5. Vilken målgrupp brukar du själv oftast skapa verksamhetsbeskrivningar för, och hur påverkar det nivån?

## Nästa steg

I nästa kapitel skapar vi en grundkarta över förmåga, process, rutin och närliggande begrepp. Där går vi från problemet med otydliga beskrivningar till en mer systematisk förståelse av vilka beskrivningstyper som finns och hur de skiljer sig från varandra.
