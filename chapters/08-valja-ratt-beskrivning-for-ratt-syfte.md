# Kapitel 8: Att välja rätt beskrivning för rätt syfte

## Varför detta kapitel finns

De tidigare kapitlen har gått igenom flera typer av verksamhetsbeskrivningar: förmågor, processer, rutiner, tjänster, produkter, värdeflöden, information, regler, roller och ansvar. Var och en av dem kan vara mycket användbar. Men de blir användbara på olika sätt.

Ett vanligt problem i verksamhetsarkitektur och verksamhetsutveckling är inte att organisationen saknar modeller. Problemet är ofta att den använder fel typ av beskrivning för frågan som ska besvaras. En förmågekarta används som om den vore en process. En processmodell används som om den vore en rutin. En rutin får bära ansvarsfördelning, informationsdefinitioner, systemkrav och undantagsregler. En tjänstekarta görs när det egentliga behovet är att förstå ett värdeflöde. En ansvarsmatris skapas när problemet egentligen är att processens resultat är otydligt.

När beskrivningen inte passar syftet uppstår flera följdproblem. Den blir svår att förstå, svår att förvalta och svår att använda som beslutsunderlag. Människor börjar tolka modellen utifrån sina egna behov, och samma bild används i strategidialog, kravarbete, utbildning och detaljstyrning trots att dessa situationer kräver olika nivåer och olika frågor.

Det här kapitlet är därför ett beslutsstöd. Målet är att hjälpa dig välja vilken typ av beskrivning som behövs, vilken nivå den bör ligga på och när flera beskrivningar behöver kombineras. Kapitlet handlar inte om att välja en enda rätt modell för alltid, utan om att välja rätt beskrivning för det aktuella syftet.

I caset med Tullmyndigheten Atlantis kan frågan “hur fungerar deklarationshanteringen?” betyda flera olika saker:

- Ledningen kan vilja förstå vilka förmågor som behöver stärkas.
- Ett utvecklingsteam kan vilja förstå vilka digitala produkter som stödjer arbetet.
- En processägare kan vilja förbättra flödet från inlämnad deklaration till beslut.
- En utbildningsansvarig kan vilja ta fram en rutin för nya handläggare.
- En informationsarkitekt kan vilja definiera vilka informationsobjekt som används.
- En säkerhetsansvarig kan vilja förstå vem som får fatta beslut och på vilken grund.

Alla frågorna rör samma verksamhetsområde, men de behöver inte samma beskrivning.

## Lärandemål

Efter kapitlet ska du kunna:

- välja beskrivningstyp utifrån syfte, målgrupp och beslutssituation
- avgöra när en förmåga, process, rutin, tjänst, produkt, värdeflöde, informationsbeskrivning, regelbeskrivning eller ansvarsfördelning är mest relevant
- känna igen när en modell försöker lösa för många problem samtidigt
- formulera analysfrågor som leder till rätt typ av beskrivning
- kombinera flera beskrivningar utan att blanda ihop deras roller
- använda ett enkelt beslutsstöd för att välja nästa steg i en analys
- förklara varför “rätt detaljnivå” beror på användningsområdet

## Innan vi börjar

I det här kapitlet använder vi en enkel princip:

> En verksamhetsbeskrivning är rätt när den hjälper rätt målgrupp att fatta rätt beslut eller utföra rätt arbete.

Det innebär att kvalitet inte bara handlar om hur korrekt, snygg eller komplett en modell är. En mycket korrekt processmodell kan vara fel om frågan handlar om strategisk förmågeutveckling. En detaljerad rutin kan vara fel om frågan handlar om ansvar på ledningsnivå. En förmågekarta kan vara fel om en handläggare behöver veta exakt vilka steg som ska utföras i ett ärende.

Tre frågor bör alltid komma före valet av beskrivning:

1. Vad ska beskrivningen användas till?
2. Vem ska använda den?
3. Vilket beslut eller vilket arbete ska den stödja?

Om dessa tre frågor är oklara är det för tidigt att välja notation, mall eller detaljnivå.

## Huvudförklaring

### Börja med användningsområdet

Användningsområdet är skälet till att beskrivningen tas fram. Det kan vara strategiskt, taktiskt eller operativt. Det kan också vara analytiskt, kommunikativt eller styrande.

Ett strategiskt användningsområde kan vara att förstå vilka förmågor Tullmyndigheten Atlantis behöver utveckla de kommande åren. Då är det oftast för tidigt att beskriva detaljerade handläggningsrutiner. Frågan handlar snarare om vad myndigheten behöver kunna och vilka förmågor som är särskilt viktiga för uppdraget.

Ett taktiskt användningsområde kan vara att förbättra ett flöde, samordna ansvar mellan avdelningar eller planera utvecklingsinsatser. Då kan processer, värdeflöden, tjänster, produkter och ansvarsfördelning bli mer relevanta.

Ett operativt användningsområde kan vara att stödja handläggare i vardagen. Då behövs ofta rutiner, instruktioner, checklistor, beslutsregler och tydliga informationskrav.

Samma verksamhetsområde kan alltså behöva beskrivas på flera sätt. Det är inte ett tecken på dubbelarbete. Det är ett tecken på att olika frågor kräver olika perspektiv.

### Utgå från frågan, inte från favoritmodellen

Många organisationer har favoritmodeller. Vissa börjar alltid med processer. Andra börjar alltid med förmågor. Några börjar med systemkarta, informationsmodell eller tjänstekarta. Det kan fungera om modellen råkar passa frågan, men det leder ofta fel om modellen väljs av vana.

Ett bättre arbetssätt är att lyssna efter vilken typ av fråga som faktiskt ställs.

Om frågan börjar med “vad behöver vi kunna?” pekar den ofta mot förmågor.

Om frågan börjar med “hur rör sig arbetet från start till mål?” pekar den ofta mot process eller värdeflöde.

Om frågan börjar med “hur ska medarbetaren göra i detta läge?” pekar den ofta mot rutin eller instruktion.

Om frågan börjar med “vilket värde erbjuder vi och till vem?” pekar den ofta mot tjänst eller produkt.

Om frågan börjar med “vilken information behöver vi förstå och hantera?” pekar den ofta mot informationsbeskrivning.

Om frågan börjar med “vad får eller måste vi göra?” pekar den ofta mot regelbeskrivning.

Om frågan börjar med “vem äger, beslutar, utför eller godkänner?” pekar den ofta mot roller och ansvar.

Frågan är sällan perfekt formulerad från början. En beställare kan säga “vi behöver en processkarta” när det verkliga behovet är att förstå ansvar, systemstöd eller förmågegap. Därför behöver du ibland översätta beställningen till ett analysbehov.

### Skillnaden mellan att förstå, styra och utföra

En viktig skillnad är om beskrivningen ska hjälpa någon att förstå, styra eller utföra.

En förståelsebeskrivning gör ett område begripligt. Den kan visa begrepp, samband, nivåer och sammanhang. Förmågekartor, tjänstekartor, värdeflöden och övergripande processbilder används ofta på detta sätt.

En styrningsbeskrivning hjälper organisationen att prioritera, fördela ansvar, följa upp eller fatta beslut. Här kan förmågor, ansvarsmatriser, principer, regelbeskrivningar, produktägarskap och processägarskap vara viktiga.

En utförandebeskrivning hjälper någon att göra arbetet rätt i praktiken. Här behövs ofta rutiner, instruktioner, checklistor, arbetssteg, systemanvisningar och undantagshantering.

Många problem uppstår när en och samma modell försöker vara alla tre samtidigt. En processkarta som ska förklara strategiskt sammanhang, visa ansvar, dokumentera systemsteg, utbilda nya medarbetare och ge ledningen beslutsunderlag kommer snabbt att bli för tung. Den kommer antingen bli för detaljerad för ledningen eller för övergripande för handläggarna.

### Beskrivningstyper och deras bästa användning

Förmågebeskrivningar är starka när du vill förstå vad organisationen behöver kunna oberoende av hur arbetet råkar vara organiserat i dag. De passar för strategi, målbild, förändringsportfölj, gap-analys, investeringar och dialog mellan verksamhet och IT. De är däremot svagare när någon behöver veta arbetsordning eller detaljerade handgrepp.

Processbeskrivningar är starka när du vill förstå hur arbete flödar över tid, vilka aktiviteter som leder till ett resultat och var överlämningar, väntetider eller brister finns. De passar för förbättring, samordning, ansvarsdialog, kravarbete och utbildning på övergripande nivå. De är däremot svagare som fullständiga instruktioner för varje situation.

Rutiner och instruktioner är starka när någon behöver veta hur ett återkommande moment ska utföras. De passar för operativ kvalitet, introduktion, regelefterlevnad och gemensamt arbetssätt. De är däremot svagare för strategisk analys, eftersom de ofta är för detaljerade och för bundna till dagens lösning.

Tjänste- och produktbeskrivningar är starka när du vill förstå vad som erbjuds, till vem och med vilken nytta. De passar när organisationen behöver förbättra mottagarupplevelse, tydliggöra produktägarskap, planera digital utveckling eller samordna verksamhet och teknik. De är däremot inte automatiskt processer, även om tjänster och produkter ofta realiseras genom processer och förmågor.

Värdeflödesbeskrivningar är starka när du vill förstå vägen från behov till realiserat värde. De passar för att hitta flaskhalsar, väntetider, onödiga överlämningar och bristande samordning. De är däremot ofta för övergripande för att ersätta rutiner.

Informationsbeskrivningar är starka när du vill förstå vilka begrepp, informationsobjekt och data som verksamheten behöver hantera. De passar för systemutveckling, integrationer, datakvalitet, rapportering, informationsägarskap och regelverk. De är däremot inte samma sak som process, även om information skapas och används i processer.

Regelbeskrivningar är starka när beslut, villkor, krav eller begränsningar behöver tydliggöras. De passar när verksamheten styrs av lag, policy, riskklassning, behörighet eller affärsregler. De är däremot inte samma sak som rutin, eftersom en regel anger vad som gäller medan rutinen beskriver hur arbetet ska utföras.

Roll- och ansvarsfördelningar är starka när ägarskap, beslut, utförande, godkännande och samverkan behöver klargöras. De passar särskilt bra när flera enheter eller roller är inblandade. De är däremot inte ett substitut för process, eftersom ansvar inte automatiskt visar flöde.

### En praktisk beslutsmatris

Följande matris kan användas som första stöd. Den ersätter inte analys, men hjälper dig välja startpunkt.

| Om huvudfrågan är | Börja med | Komplettera ofta med |
|---|---|---|
| Vad behöver organisationen kunna? | Förmågebeskrivning | Målbild, gap, investeringar, processer |
| Hur skapas resultat över tid? | Processbeskrivning | Roller, information, regler, systemstöd |
| Hur ska arbetet utföras i praktiken? | Rutin eller instruktion | Regler, checklistor, systemanvisningar |
| Vilket värde erbjuder vi och till vem? | Tjänste- eller produktbeskrivning | Förmågor, värdeflöden, mottagarbehov |
| Hur rör sig behov till nytta? | Värdeflöde | Processer, produkter, flaskhalsanalys |
| Vilken information behöver vi hantera? | Informationsbeskrivning | Processer, system, regler, ägarskap |
| Vad styr beslut och tillåtna handlingsalternativ? | Regelbeskrivning | Rutiner, processer, ansvar |
| Vem äger, beslutar, utför eller godkänner? | Roll- och ansvarsfördelning | Processer, rutiner, styrmodell |
| Vilka system stödjer verksamheten? | System- eller applikationskarta | Förmågor, processer, information |
| Var finns förändringsbehovet? | Förmågor eller värdeflöde | Processer, produkter, data, ansvar |

Matrisen visar också att många frågor kräver kombinationer. Att börja med förmågor betyder inte att processer är oviktiga. Att börja med processer betyder inte att roller och information kan lämnas otydliga. Valet av startpunkt handlar om vilken beskrivning som bäst fångar det viktigaste problemet.

### Exempel: samma situation, olika beskrivningar

Anta att Tullmyndigheten Atlantis upplever att hanteringen av importdeklarationer tar för lång tid och att det finns variation mellan olika kontor. Flera personer säger att “processen behöver beskrivas”. Det kan vara sant, men det kan också vara för snabbt sagt.

Om problemet är att myndigheten saknar samsyn om vilka förmågor som behövs för modern deklarationshantering bör arbetet börja med förmågor. Då kan relevanta förmågor vara exempelvis **Ta emot deklaration**, **Riskbedöma deklaration**, **Fatta tullbeslut**, **Kommunicera med uppgiftslämnare** och **Följa upp efterlevnad**.

Om problemet är att ärenden fastnar mellan roller och organisatoriska enheter bör arbetet börja med process eller värdeflöde. Då behöver man se flödet från inlämnad deklaration till beslut, inklusive väntetider, överlämningar och återkoppling.

Om problemet är att handläggare gör olika bedömningar i liknande situationer kan regelbeskrivningar och rutiner vara viktigare än en ny processkarta. Då behöver man tydliggöra bedömningsregler, undantag och praktiska instruktioner.

Om problemet är att systemutvecklingsteamet inte förstår vilka uppgifter som behövs i olika steg kan informationsbeskrivning vara startpunkten. Då behöver begrepp som deklaration, varupost, uppgiftslämnare, riskindikator, kontrollbeslut och kompletteringsbegäran definieras.

Om problemet är att ingen vet vem som får besluta om vissa avvikelser behövs roll- och ansvarsfördelning. Då är det inte säkert att en mer detaljerad process löser problemet.

Samma verksamhetsområde kan alltså ge minst fem olika analysstarter. Det är därför frågan “vad ska modellen användas till?” är så viktig.

### När flera beskrivningar behövs

I praktiken räcker det sällan med en enda beskrivning. Men flera beskrivningar måste hållas ihop på ett kontrollerat sätt.

En bra kombination kan se ut så här:

- En förmågekarta visar vad Tullmyndigheten Atlantis behöver kunna.
- Ett värdeflöde visar hur behov blir till resultat.
- En processbeskrivning visar huvudstegen i arbetet.
- Rutiner visar hur kritiska moment utförs.
- Informationsbeskrivningar definierar centrala informationsobjekt.
- Regelbeskrivningar visar vilka villkor och krav som styr beslut.
- En ansvarsmatris visar ägarskap, utförande och godkännande.
- En produktkarta visar vilka digitala produkter som stödjer arbetet.

Det viktiga är att varje beskrivning får ett tydligt ansvar. Förmågekartan ska inte behöva visa alla arbetssteg. Processen ska inte behöva definiera alla informationsobjekt. Rutinen ska inte behöva bära hela styrmodellen. Produktkartan ska inte behöva förklara hela verksamhetens uppdrag.

När flera beskrivningar används behöver relationerna mellan dem vara tydliga. En process kan realisera en förmåga. En rutin kan detaljera ett processteg. En regel kan styra ett beslut i processen. Ett informationsobjekt kan användas i flera processteg. En digital produkt kan stödja flera förmågor. En roll kan ha ansvar i flera processer.

Det är relationerna som skapar helhet, inte att allt pressas in i en enda modell.

### Rätt detaljnivå är en konsekvens av syftet

Detaljnivå är en av de vanligaste konfliktpunkterna. Någon tycker att modellen är för övergripande. Någon annan tycker att den är för detaljerad. Båda kan ha rätt, om de tänker på olika användningsområden.

En ledningsgrupp behöver ofta förstå mönster, prioriteringar, risker och beroenden. Den behöver sällan se varje operativt steg.

En processägare behöver förstå flöde, ansvar, resultat och förbättringsområden. Processägaren behöver mer detaljer än ledningen, men inte nödvändigtvis fullständiga systeminstruktioner.

En handläggare behöver veta vad som ska göras, i vilken ordning, vilka undantag som finns och vilka regler som gäller. Där kan detaljnivån behöva vara hög.

Ett utvecklingsteam behöver ofta detaljer om information, regler, integrationer, användningsfall och avvikelser. Men teamet behöver också förstå det större sammanhanget, annars riskerar lösningen att optimera en liten del av verksamheten på bekostnad av helheten.

Frågan är alltså inte “hur detaljerad ska modellen vara?” utan “hur detaljerad behöver beskrivningen vara för att stödja sitt användningsområde?”.

### Tecken på att du har valt fel beskrivning

Det finns flera varningssignaler:

- Modellen växer snabbt och får fler och fler typer av information.
- Olika målgrupper vill ha helt olika detaljer i samma bild.
- Beskrivningen blir svår att förklara utan lång muntlig genomgång.
- Ingen vet om modellen är en nulägesbild, målbild, instruktion eller beslutsunderlag.
- Diskussionen fastnar i notation i stället för verksamhetsfråga.
- Samma objekt byter betydelse beroende på vem som läser modellen.
- Modellen används för att lösa ansvar, informationsdefinitioner och arbetsflöde samtidigt.
- Det är oklart vem som ska förvalta beskrivningen efter workshopen.

När du ser dessa signaler bör du inte nödvändigtvis rita mer. Ofta behöver du backa och fråga vilken typ av beskrivning som egentligen behövs.

### Från beställning till analysbehov

En beställning är ofta formulerad som ett önskat resultat: “vi behöver en processkarta”, “vi behöver en förmågemodell”, “vi behöver dokumentera våra rutiner”. En analysledares uppgift är att förstå behovet bakom beställningen.

Du kan använda följande frågor:

- Vilket problem ska beskrivningen hjälpa oss att lösa?
- Vilka beslut ska fattas med hjälp av beskrivningen?
- Vem ska använda den efter att den är framtagen?
- Är syftet att förstå nuläge, beskriva målbild, styra förändring eller stödja utförande?
- Behöver vi visa vad organisationen behöver kunna, hur arbete flödar, hur arbete utförs, vem som ansvarar eller vilken information som används?
- Vilken nivå är användbar för målgruppen?
- Vad händer om vi inte gör beskrivningen?
- Hur ska beskrivningen förvaltas?

Dessa frågor gör att du kan översätta beställningen till ett tydligare uppdrag. Ibland blir svaret att beställaren faktiskt behöver en process. Ibland visar det sig att processkartan bara var ett ord för “vi behöver förstå hur området hänger ihop”.

## Exempel

### Exempel 1: Ledningen vill prioritera investeringar

Tullmyndighetens ledning vill prioritera vilka utvecklingsinsatser som ska finansieras kommande år. Flera initiativ konkurrerar om resurser: förbättrad riskanalys, modernisering av deklarationsmottagning, bättre självservice och ökad spårbarhet i kontrollbeslut.

En detaljerad processmodell kan ge viss förståelse, men den är inte bästa startpunkt. Ledningen behöver först se vilka förmågor som är strategiskt viktiga, vilka som är svaga och vilka som har stark koppling till myndighetens mål.

Lämplig start:

- förmågekarta
- förmågebedömning
- koppling till mål, risker och pågående initiativ

Möjliga komplement:

- värdeflöde för att visa konsekvenser för helheten
- produktkarta för att visa digitalt stöd
- ansvarsfördelning för förmågeägarskap

### Exempel 2: Handläggare gör olika i liknande ärenden

Ett kontor upptäcker att liknande deklarationer hanteras olika beroende på handläggare. Den första reaktionen är att processen behöver beskrivas tydligare.

Efter några frågor visar det sig att processens huvudsteg redan är kända. Problemet ligger i bedömningar, undantag och lokala tolkningar. Då räcker det inte att rita om processflödet.

Lämplig start:

- regelbeskrivning
- rutin för bedömning och eskalering
- exempel på typfall

Möjliga komplement:

- processbeskrivning för att visa var bedömningen sker
- roll- och ansvarsfördelning för beslut och granskning
- informationsbeskrivning för vilka uppgifter som krävs

### Exempel 3: Ett utvecklingsteam ska bygga nytt stöd

Ett team ska utveckla ett digitalt stöd för kompletteringsbegäran. Teamet frågar efter “processen”. De behöver förstå flödet, men de behöver också mer än så.

Lämplig start:

- processbeskrivning på lagom nivå
- informationsbeskrivning för kompletteringsbegäran, ärende, uppgiftslämnare och beslut
- regelbeskrivning för när komplettering krävs
- produktbeskrivning för det digitala stödet

Möjliga komplement:

- rutin för operativ hantering
- ansvarsmatris mellan handläggare, system och granskare
- förmågekarta för att visa vilket större område produkten stödjer

### Exempel 4: En workshop fastnar i begreppsdiskussion

En workshop ska beskriva “kontrollprocessen”. Efter en timme diskuterar deltagarna om riskanalys är en process, en förmåga, en aktivitet, ett system eller en organisatorisk funktion.

Det är ett tecken på att gruppen blandar perspektiv. Lösningen är inte att välja ett ord för allt, utan att separera frågorna.

Ett möjligt upplägg:

- Beskriv **Riskbedöma och prioritera kontrollinsatser** som förmåga.
- Beskriv **Planera och genomföra kontroll** som process eller värdeflöde.
- Beskriv **Utföra dokumentkontroll** som rutin om det behövs på detaljnivå.
- Beskriv riskindikatorer och kontrollunderlag som informationsobjekt.
- Beskriv beslutskriterier som regler.
- Beskriv kontrollant, beslutsfattare och kvalitetsgranskare som roller.

Då kan varje begrepp användas där det gör mest nytta.

## Praktiskt arbetssätt

### Steg 1: Formulera användningsområdet

Skriv en enkel mening:

> Den här beskrivningen ska hjälpa [målgrupp] att [beslut eller arbete] genom att visa [perspektiv].

Exempel:

> Den här beskrivningen ska hjälpa processägare att identifiera förbättringsområden genom att visa huvudflödet från inkommen deklaration till beslut.

Ett annat exempel:

> Den här beskrivningen ska hjälpa ledningen att prioritera utvecklingsinitiativ genom att visa vilka förmågor som är mest kritiska och vilka som behöver stärkas.

Om du inte kan fylla i meningen är syftet för otydligt.

### Steg 2: Välj primär beskrivning

Välj en primär beskrivning som svarar på huvudfrågan. Undvik att börja med flera modeller samtidigt om gruppen inte är van. Det är ofta bättre att skapa en enkel startpunkt och sedan komplettera.

Fråga:

- Är huvudfrågan vad vi behöver kunna?
- Är huvudfrågan hur arbetet flödar?
- Är huvudfrågan hur arbetet ska utföras?
- Är huvudfrågan vilket värde som erbjuds?
- Är huvudfrågan vilken information som krävs?
- Är huvudfrågan vilka regler som styr?
- Är huvudfrågan vem som ansvarar?

### Steg 3: Bestäm nivå

Bestäm vilken nivå som är relevant innan workshopen börjar. Ange också vad som inte ska beskrivas.

Exempel:

- Vi ska beskriva huvudprocessen, inte detaljerade systemklick.
- Vi ska identifiera förmågor på nivå 1 och 2, inte aktiviteter.
- Vi ska beskriva rutinen för kompletteringsbegäran, inte hela deklarationsflödet.
- Vi ska definiera centrala informationsobjekt, inte varje datafält.
- Vi ska klargöra ansvar för beslut, inte beskriva varje roll i organisationen.

Avgränsningen är inte en begränsning av kvalitet. Den är en förutsättning för användbarhet.

### Steg 4: Identifiera nödvändiga komplement

När den primära beskrivningen är vald kan du fråga vilka kompletterande perspektiv som behövs.

En process kan behöva kompletteras med roller, information och regler. En förmågekarta kan behöva kompletteras med bedömningar, initiativ och ägarskap. En rutin kan behöva kompletteras med regelreferenser och exempel. En produktbeskrivning kan behöva kompletteras med tjänst, mottagare, förmågor och systemberoenden.

Komplementen ska läggas till för att de behövs, inte för att modellen ska bli komplett i största möjliga mening.

### Steg 5: Bestäm förvaltning

Innan beskrivningen blir “klar” bör någon kunna svara på:

- Vem äger beskrivningen?
- När ska den uppdateras?
- Vilka beslut eller arbetssätt påverkas av den?
- Var ska den publiceras?
- Hur vet vi om den fortfarande är aktuell?
- Vilka andra beskrivningar behöver den vara konsekvent med?

En beskrivning som inte förvaltas blir snabbt en dokumentationsrest. Det är särskilt riskabelt för rutiner, ansvar, regler och systemnära information, eftersom de förändras oftare än övergripande förmågor.

## Vanliga misstag

- **Misstag: Att börja med notation i stället för fråga.**
  - Varför det händer: Organisationen har mallar, verktyg eller ramverk som styr arbetet.
  - Hur du undviker det: Formulera först användningsområde, målgrupp och beslutssituation.

- **Misstag: Att använda process för allt.**
  - Varför det händer: Process är ett välkänt ord som många uppfattar som neutralt.
  - Hur du undviker det: Kontrollera om frågan egentligen handlar om förmåga, ansvar, information, regel eller rutin.

- **Misstag: Att använda förmågor som aktiviteter.**
  - Varför det händer: Gruppen börjar tänka på vad människor gör i vardagen.
  - Hur du undviker det: Testa om formuleringen beskriver vad organisationen behöver kunna, inte ett steg i ett flöde.

- **Misstag: Att göra rutiner för strategiska frågor.**
  - Varför det händer: Det känns konkret och handlingsorienterat att skriva instruktioner.
  - Hur du undviker det: Säkerställ att syftet verkligen är operativt utförande, inte prioritering eller målbild.

- **Misstag: Att blanda nuläge och målbild utan att markera det.**
  - Varför det händer: Deltagare vill både beskriva hur det är och hur det borde vara.
  - Hur du undviker det: Märk tydligt vad som är nuläge, målbild, princip, problem eller beslut.

- **Misstag: Att lägga in för mycket i samma modell.**
  - Varför det händer: Man vill undvika flera dokument eller är rädd att tappa helheten.
  - Hur du undviker det: Skapa flera enkla beskrivningar med tydliga relationer i stället för en överlastad modell.

- **Misstag: Att välja detaljnivå efter den mest detaljintresserade deltagaren.**
  - Varför det händer: Detaljfrågor känns konkreta och kan dominera workshops.
  - Hur du undviker det: Håll fast vid målgruppen och användningsområdet. Parkera detaljer som hör hemma i annan beskrivning.

- **Misstag: Att glömma förvaltningen.**
  - Varför det händer: Fokus ligger på att producera modellen, inte på dess liv efter projektet.
  - Hur du undviker det: Bestäm ägare, uppdateringstillfälle och publiceringsplats innan beskrivningen används brett.

## Övningar

### Övning 1: Översätt beställningen

Utgå från följande beställningar och formulera vilket analysbehov som kan ligga bakom.

1. “Vi behöver en processkarta för importflödet.”
2. “Vi behöver dokumentera våra rutiner.”
3. “Vi behöver förstå vilka system som stödjer kontrollverksamheten.”
4. “Vi behöver en gemensam bild av våra förmågor.”
5. “Vi behöver tydliggöra vem som ansvarar för riskbeslut.”

För varje beställning, svara på:

- Vilken målgrupp kan tänkas behöva beskrivningen?
- Vilket beslut eller arbete ska den stödja?
- Vilken beskrivningstyp är trolig startpunkt?
- Vilka kompletterande beskrivningar kan behövas?

### Övning 2: Välj beskrivningstyp

Läs situationerna nedan och välj primär beskrivning.

1. Ledningen vill prioritera investeringar för kommande tre år.
2. Ett team vill minska ledtiden från inkommen deklaration till beslut.
3. Nya handläggare behöver veta exakt hur komplettering ska begäras.
4. Flera avdelningar är oense om vem som äger en viss information.
5. Juridikfunktionen vill tydliggöra vilka regler som styr ett kontrollbeslut.
6. En produktägare vill förstå vilka användarbehov ett digitalt stöd ska möta.

Motivera varje val med en mening.

### Övning 3: Skriv användningsmeningen

Välj ett område i din egen verksamhet och fyll i meningen:

> Den här beskrivningen ska hjälpa [målgrupp] att [beslut eller arbete] genom att visa [perspektiv].

Skriv sedan:

- primär beskrivningstyp
- önskad detaljnivå
- vad som uttryckligen inte ska beskrivas
- vilka komplement som sannolikt behövs
- vem som bör äga beskrivningen

### Fördjupning

Välj en befintlig modell i din organisation. Granska den med följande frågor:

- Vilket användningsområde verkar modellen ha?
- Vilken målgrupp verkar den vara gjord för?
- Vilken beskrivningstyp är den egentligen?
- Försöker den lösa flera olika frågor samtidigt?
- Finns det information i modellen som borde ligga i en annan typ av beskrivning?
- Är detaljnivån rimlig för målgruppen?
- Är det tydligt om modellen visar nuläge, målbild eller beslutad styrning?
- Vem verkar äga och förvalta modellen?

Skriv en rekommendation: behåll som den är, förenkla, dela upp, komplettera eller ersätt.

## Snabb sammanfattning

- Välj beskrivning utifrån användningsområde, målgrupp och beslutssituation.
- En förmåga beskriver vad organisationen behöver kunna.
- En process beskriver hur arbete skapar resultat över tid.
- En rutin beskriver hur återkommande arbete utförs i praktiken.
- En tjänst eller produkt beskriver vilket värde som erbjuds och till vem.
- Ett värdeflöde visar vägen från behov till realiserad nytta.
- Information, regler, roller och ansvar kompletterar andra beskrivningar.
- En modell som försöker lösa alla frågor samtidigt blir ofta svår att använda.
- Rätt detaljnivå beror på vad beskrivningen ska användas till.
- Flera enkla beskrivningar med tydliga relationer är ofta bättre än en överlastad modell.

## Quiz/reflektionsfrågor

1. Varför är det riskabelt att börja med en bestämd modelltyp innan användningsområdet är formulerat?
2. När är en förmågebeskrivning en bättre startpunkt än en processbeskrivning?
3. När är en rutin mer relevant än en process?
4. Vilka frågor pekar mot informationsbeskrivning?
5. Vad är skillnaden mellan att beskriva för att förstå, styra och utföra?
6. Vilka varningssignaler visar att en modell försöker bära för mycket?
7. Hur kan du avgöra om detaljnivån är rimlig?
8. Varför är förvaltning en del av valet av beskrivningstyp?

## Nästa steg

När rätt beskrivningstyp är vald återstår fortfarande en svår del: att identifiera och avgränsa det som ska beskrivas. Nästa kapitel handlar därför om hur du går från otydliga utsagor, workshopdiskussioner och verksamhetsproblem till tydliga kandidater för förmågor, processer, rutiner, information, regler och ansvar.

Där går vi från beslutsstöd till praktisk analysmetod.
