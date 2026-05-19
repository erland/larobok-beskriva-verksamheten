# Kapitel 2: Grundkartan: förmåga, process, rutin och närliggande begrepp

## Varför detta kapitel finns

I många verksamhetsbeskrivningar uppstår förvirringen inte för att någon saknar kompetens, utan för att flera olika saker beskrivs samtidigt. En grupp pratar om vad organisationen behöver kunna. En annan pratar om hur arbete flödar. En tredje försöker skriva ned exakt hur en handläggare ska göra i ett visst system. Alla tre kan ha rätt, men de gör olika typer av beskrivningar.

Det här kapitlet ger en grundkarta över de vanligaste beskrivningstyperna i boken: förmåga, process, rutin, tjänst, värdeflöde, information, regel, roll och ansvar. Målet är inte att skapa akademiskt perfekta definitioner. Målet är att ge ett praktiskt språk som hjälper verksamhetsarkitekter, IT-arkitekter och verksamhetsutvecklare att välja rätt beskrivning för rätt syfte.

I det återkommande caset använder vi Tullmyndigheten Atlantis, en fiktiv tullmyndighet. Den hanterar deklarationer, riskbedömningar, kontroller, ärenden, regelverk och digitala tjänster. Exemplen är förenklade för att visa skillnader mellan beskrivningstyper, inte för att beskriva en faktisk myndighets arbetssätt.

## Lärandemål

Efter kapitlet ska du kunna:

- Förklara skillnaden mellan förmåga, process och rutin på ett praktiskt sätt.
- Känna igen när en beskrivning egentligen handlar om tjänst, värdeflöde, information, regel, roll eller ansvar.
- Sortera otydliga utsagor efter vilken typ av verksamhetsbeskrivning de främst pekar mot.
- Välja en rimlig första beskrivningstyp utifrån syfte och målgrupp.
- Undvika att blanda abstraktionsnivåer i samma modell.

## Innan vi börjar

I kapitel 1 etablerades tre frågor som styr en användbar verksamhetsbeskrivning:

- Vad ska beskrivningen användas till?
- Vem ska använda den?
- Vilken nivå behöver den ligga på?

De frågorna följer med in i detta kapitel. En förmåga, en process och en rutin är inte konkurrerande svar på samma fråga. De svarar på olika frågor. Därför behöver vi först förstå vilken fråga vi försöker besvara.

## Kortversion: vad skiljer begreppen åt?

En första sortering kan göras med några enkla frågor. Tabellen är inte en fullständig metod, men den hjälper dig att höra vad en diskussion egentligen handlar om.

| Begrepp | Fråga det främst besvarar | Typiskt användningsområde |
|---|---|---|
| Förmåga | Vad behöver organisationen kunna? | Strategi, förändringsanalys, målbild och prioritering |
| Process | Hur skapas ett resultat över tid? | Förbättring, ansvar, överlämningar och flödesförståelse |
| Rutin | Hur ska ett återkommande arbete utföras i praktiken? | Utförandestöd, kvalitetssäkring och introduktion |
| Tjänst | Vad erbjuds en mottagare? | Kund-/användarperspektiv, serviceutveckling och uppdrag |
| Produkt | Vad utvecklas och förvaltas som ett avgränsat erbjudande eller lösningsområde? | Produktstyrning, team, backlogg och livscykel |
| Värdeflöde | Hur rör sig behov till nytta på övergripande nivå? | Helhetssyn, prioritering och end-to-end-förståelse |
| Information | Vilka uppgifter behöver verksamheten förstå och hantera? | Informationsmodellering, begreppsförståelse och systemstöd |
| Regel | Vilka villkor styr beslut eller agerande? | Beslutslogik, regelefterlevnad och kravarbete |
| Roll och ansvar | Vem gör, äger, beslutar eller säkerställer något? | Styrning, ansvarsfördelning och förvaltning |


## Grundprincipen: olika beskrivningar svarar på olika frågor

En enkel tumregel är att lyssna efter frågeordet.

| Fråga | Ofta lämplig beskrivning |
|---|---|
| Vad behöver organisationen kunna? | Förmåga |
| Hur skapas ett resultat över tid? | Process eller värdeflöde |
| Hur ska arbetet utföras i praktiken? | Rutin eller instruktion |
| Vad erbjuds en mottagare? | Tjänst eller produkt |
| Vilken information behöver verksamheten hantera? | Informationsobjekt eller informationsmodell |
| Vilka regler styr beslut och agerande? | Affärsregel eller regelbeskrivning |
| Vem gör, äger eller beslutar vad? | Roll, ansvar eller ansvarsmatris |

Tabellen är inte en absolut sanning, men den ger ett första sorteringsstöd. Om någon säger “vi behöver beskriva processen för riskbedömning” kan det i praktiken betyda flera saker. Personen kanske vill förstå förmågan att riskbedöma varuflöden, flödet från deklaration till kontrollbeslut, en rutin för manuell riskgranskning eller ansvarsfördelningen mellan olika roller.

Det första steget är därför inte att välja notation eller mall. Det första steget är att förstå vilken fråga som behöver besvaras.

## Förmåga: vad organisationen behöver kunna göra

En förmåga beskriver vad organisationen behöver kunna göra för att uppfylla sitt uppdrag eller skapa värde. Förmågan är ofta mer stabil än processer, organisation och system. Den säger inte i första hand hur arbetet utförs, vem som gör det eller vilket system som används.

I en tullmyndighet kan exempel på förmågor vara:

- Riskbedöma varuflöden.
- Hantera inkommande deklarationer.
- Genomföra kontrollåtgärder.
- Tillhandahålla digital självservice.
- Förvalta regelverkstolkning.

En bra förmågebeskrivning är vanligtvis formulerad som ett verksamhetskunnande. Den pekar på något organisationen måste kunna göra även om organisation, teknik eller arbetssätt förändras.

### När förmågebeskrivningen är användbar

Förmågor passar särskilt bra när syftet är att:

- skapa en stabil karta över vad verksamheten behöver kunna,
- koppla strategi till förändringsinitiativ,
- analysera styrkor, svagheter, mognad eller utvecklingsbehov,
- förstå vilka delar av verksamheten som påverkas av en förändring,
- koppla verksamhetsbehov till systemstöd, information, ansvar och investeringar.

Om Tullmyndigheten Atlantis ska modernisera sin digitala service kan en förmågekarta visa vilka förmågor som påverkas. Den kan visa att moderniseringen inte bara handlar om en e-tjänst, utan också om kundstöd, regelverkstolkning, informationshantering, riskbedömning och uppföljning.

### Vanlig sammanblandning

En vanlig fallgrop är att beskriva förmågor som aktiviteter. “Ta emot deklaration” låter som ett steg i ett flöde, medan “Hantera inkommande deklarationer” tydligare pekar på ett kunnande som kan behövas över tid. Skillnaden är inte alltid skarp, men formuleringen påverkar hur beskrivningen används.

Ett nivåtest är att fråga:

- Skulle detta fortfarande behövas om organisationen ändrade arbetssätt?
- Skulle detta fortfarande vara relevant om ett nytt system infördes?
- Beskriver vi vad verksamheten behöver kunna, snarare än hur arbetet går till?

Om svaret är ja kan det vara en förmåga.

## Process: hur arbete skapar resultat över tid

En process beskriver hur arbete flödar över tid för att skapa ett resultat för en mottagare. Den visar ofta aktiviteter, händelser, beslutspunkter, överlämningar och resultat. Där förmågan svarar på vad organisationen behöver kunna, svarar processen på hur arbete faktiskt eller önskat rör sig från start till slut.

I en tullmyndighet kan en process vara:

- Ta emot deklaration.
- Granska deklaration.
- Begära komplettering.
- Riskbedöma ärende.
- Besluta om kontrollåtgärd.
- Genomföra kontroll.
- Avsluta ärende och kommunicera beslut.

Detta är en förenklad processkedja. Den visar ett flöde, inte bara ett kunnande.

### När processbeskrivningen är användbar

Processer passar särskilt bra när syftet är att:

- förstå hur arbete rör sig mellan roller, enheter eller system,
- hitta väntetider, dubbelarbete, flaskhalsar eller överlämningsproblem,
- skapa gemensam förståelse för nuläge eller önskat läge,
- förbättra kvalitet, effektivitet eller samordning,
- koppla aktiviteter till ansvar, information och systemstöd.

Om Tullmyndigheten Atlantis har långa ledtider i ärendehantering är en processbeskrivning ofta mer användbar än en förmågekarta. Förmågekartan kan visa vilka områden som berörs, men processen visar var arbetet fastnar.

### Vanlig sammanblandning

En vanlig fallgrop är att processen blir ett organisationsschema. Om modellen framför allt visar avdelningar, linjechefer eller organisatoriska enheter beskriver den kanske inte processen. En annan fallgrop är att processen blir en systemkarta där varje steg motsvarar en knapptryckning eller skärmbild.

Ett nivåtest är att fråga:

- Finns det ett tydligt startläge och ett resultat?
- Visar beskrivningen arbete över tid?
- Går det att följa hur något förädlas, beslutas eller lämnas vidare?

Om svaret är ja kan det vara en process.

## Rutin: hur ett återkommande arbete utförs i praktiken

En rutin beskriver hur ett återkommande arbete ska utföras i praktiken. Den är mer detaljerad än en process och ofta närmare vardagens utförande. Rutinen kan innehålla steg, kontroller, ansvar, undantag, systemmoment, dokumentation och hänvisningar till regler.

I en tullmyndighet kan en rutin vara:

- Registrera inkommet underlag i ärendehanteringssystemet.
- Skicka begäran om komplettering.
- Dokumentera manuell riskgranskning.
- Kontrollera att beslut har expedierats.
- Hantera avvikelse när deklarationsuppgifter saknas.

Rutinen är inte i första hand en översikt. Den ska hjälpa någon att göra arbetet på ett konsekvent sätt.

### När rutinbeskrivningen är användbar

Rutiner passar särskilt bra när syftet är att:

- skapa enhetligt utförande,
- minska personberoende,
- stödja introduktion av nya medarbetare,
- säkerställa regelefterlevnad,
- förtydliga undantag och praktiska handgrepp,
- koppla arbetssteg till system, mallar och dokumentation.

Om problemet är att olika handläggare hanterar kompletteringsbegäranden på olika sätt kan en rutin vara mer användbar än en ny processmodell. Processen kan visa att komplettering ingår i flödet, men rutinen beskriver hur kompletteringen ska göras.

### Vanlig sammanblandning

En vanlig fallgrop är att rutinen blir för generell och därmed inte hjälper utförandet. En annan är att processmodellen fylls med rutinens alla detaljer. Då blir processen tung, svårläst och svår att använda för analys.

Ett nivåtest är att fråga:

- Är målgruppen personer som ska utföra arbetet?
- Behöver beskrivningen ange praktiska steg, undantag eller kontrollpunkter?
- Skulle beskrivningen behöva ändras om systemets arbetsflöde ändras?

Om svaret är ja kan det vara en rutin eller instruktion.

## Tjänst: vad som erbjuds en mottagare

En tjänst beskriver något verksamheten erbjuder en mottagare. Mottagaren kan vara extern, intern eller en annan del av organisationen. En tjänst är inte samma sak som en process, även om en process ofta behövs för att leverera tjänsten.

I Tullmyndigheten Atlantis case kan en tjänst vara:

- Digital tullklarering.
- Rådgivning om tullregler.
- Självservice för deklarationsstatus.
- Hantering av kontrollärende.
- Tillgång till beslutsunderlag för annan myndighet.

Tjänsten beskriver vad mottagaren får eller kan använda. Processen beskriver hur tjänsten levereras. Förmågor beskriver vad organisationen behöver kunna för att tjänsten ska fungera.

### Ett praktiskt sätt att skilja tjänst från process

Fråga vem som upplever resultatet.

Om fokus ligger på mottagarens nytta, åtkomst eller erbjudande är det ofta en tjänst. Om fokus ligger på arbetsflödet som skapar resultatet är det ofta en process.

Exempel:

- “Digital tullklarering” pekar mot en tjänst.
- “Hantera digital deklaration från inskick till beslut” pekar mot en process.
- “Tillhandahålla digital självservice” pekar mot en förmåga.
- “Kontrollera att obligatoriska fält är ifyllda innan inskick” pekar mot en regel eller rutin, beroende på sammanhang.

## Värdeflöde: hur värde skapas från behov till resultat

Ett värdeflöde beskriver en övergripande sekvens från ett behov till ett resultat. Det ligger ofta på en högre nivå än en detaljerad process och används för att förstå hur flera förmågor, processer, roller, system och informationsflöden samverkar.

I Tullmyndigheten Atlantis case kan ett värdeflöde beskrivas som:

- Aktör behöver föra in eller ut varor.
- Deklaration lämnas in.
- Uppgifter valideras och riskbedöms.
- Eventuell kontroll genomförs.
- Beslut kommuniceras.
- Varuflöde kan fortsätta eller åtgärd krävs.
- Uppföljning och lärande sker.

Värdeflödet visar den större rörelsen. Det är användbart när man vill förstå helheten innan man går ner i enskilda processer eller rutiner.

### När värdeflödet är användbart

Värdeflöden passar särskilt bra när syftet är att:

- skapa helhetsförståelse över organisatoriska gränser,
- visa hur flera processer hänger ihop,
- diskutera kund- eller aktörsnytta,
- identifiera större förbättringsområden,
- koppla strategiska mål till operativ utveckling.

En risk är att värdeflödet blir så övergripande att det inte hjälper praktiskt arbete. Därför bör det ofta kompletteras med förmågor, processer eller tjänster beroende på syftet.

## Information och informationsobjekt: vad verksamheten behöver veta

Många modeller blir röriga eftersom information blandas ihop med aktiviteter. Information är inte ett steg i processen. Den är något verksamheten behöver skapa, ta emot, bedöma, ändra, lagra, dela eller fatta beslut utifrån.

I Tullmyndigheten Atlantis case kan informationsobjekt vara:

- Deklaration.
- Varupost.
- Aktör.
- Riskindikator.
- Kontrollbeslut.
- Kompletteringsbegäran.
- Regelverkstolkning.

Informationsobjekt hjälper till att förklara vad verksamheten behöver ha kunskap om. De kan kopplas till processer, förmågor, system och regler, men bör inte pressas in som aktivitetssteg.

### När informationsbeskrivningen är användbar

Informationsbeskrivningar passar särskilt bra när syftet är att:

- klargöra begrepp och databehov,
- minska missförstånd mellan verksamhet och IT,
- förbättra informationskvalitet,
- identifiera masterdata eller centrala informationsobjekt,
- förstå vilka uppgifter som behövs för beslut, analys eller uppföljning.

Om flera delar av Tullmyndigheten Atlantis använder ordet “ärende” på olika sätt är en informations- eller begreppsmodell ofta viktigare än ännu en processkarta.

## Regler: vad som styr beslut och agerande

Regler beskriver villkor, begränsningar eller principer som styr verksamhetens beslut och agerande. De kan komma från lag, policy, interna riktlinjer, avtal, riskmodeller eller beslutade arbetssätt.

I Tullmyndigheten Atlantis case kan regler handla om:

- när en deklaration måste kompletteras,
- vilka uppgifter som krävs för viss varutyp,
- när ett ärende ska eskaleras,
- vilka kriterier som påverkar riskbedömning,
- vem som får fatta ett visst beslut.

En regel är inte samma sak som en aktivitet. Regeln kan påverka vilken aktivitet som ska utföras, men den bör kunna beskrivas som ett styrande villkor.

### När regelbeskrivningen är användbar

Regelbeskrivningar passar särskilt bra när syftet är att:

- göra beslutskriterier tydliga,
- separera styrning från arbetsflöde,
- minska variation i bedömningar,
- stödja automatisering eller kravställning,
- visa vilka beslut som är bundna av regelverk och vilka som kräver professionell bedömning.

Om en processmodell innehåller många “om detta, annars detta”-grenar kan det vara ett tecken på att vissa delar bör beskrivas som regler i stället för som processdetaljer.

## Roller och ansvar: vem som gör, äger eller beslutar

Roller och ansvar beskriver vem som utför, beslutar, äger, granskar, informeras eller följer upp något. Roller ska inte blandas ihop med organisatoriska enheter eller befattningar, även om de ofta kopplas till dem.

I Tullmyndigheten Atlantis case kan roller vara:

- Handläggare.
- Riskanalytiker.
- Kontrollansvarig.
- Tjänsteägare.
- Processägare.
- Förmågeansvarig.
- Systemförvaltare.

Ansvar kan beskrivas med enkla ansvarsmatriser eller tydliga ansvarspunkter. Det viktiga är att ansvaret kopplas till rätt sak: en process, en förmåga, en rutin, en tjänst, ett informationsobjekt eller en regel.

### När ansvar behöver beskrivas separat

Ansvar behöver ofta beskrivas separat när:

- flera roller deltar i samma process,
- ingen tydligt äger helheten,
- beslut fattas på oklara grunder,
- förvaltning av modeller, regler eller information saknas,
- verksamhet och IT har olika bild av vem som ansvarar för vad.

Om en processmodell försöker visa allt ansvar med långa texter i varje aktivitet blir den snabbt svårläst. Då kan en separat ansvarsmatris vara bättre.

## Samma situation kan beskrivas på flera sätt

Ta exemplet “hantera kompletteringsbegäran”. Det kan beskrivas på flera olika sätt beroende på syfte.

| Perspektiv | Möjlig beskrivning | Exempel på fråga |
|---|---|---|
| Förmåga | Hantera kompletteringsbehov | Vad behöver organisationen kunna? |
| Process | Begära, ta emot och bedöma komplettering | Hur rör sig arbetet från behov till beslut? |
| Rutin | Skicka kompletteringsbegäran i ärendehanteringssystemet | Hur gör handläggaren i praktiken? |
| Tjänst | Digital komplettering för deklarant | Vad erbjuds mottagaren? |
| Information | Kompletteringsbegäran och kompletteringsunderlag | Vilken information behövs? |
| Regel | När komplettering krävs | Vilka villkor styr agerandet? |
| Ansvar | Vem får begära, granska och godkänna komplettering | Vem gör eller beslutar vad? |

Det betyder inte att alla beskrivningar alltid behövs. Det betyder att samma verklighet kan betraktas genom olika linser. Den professionella uppgiften är att välja den lins som stödjer syftet.

## Praktiskt sorteringsstöd

När du möter en otydlig utsaga kan du sortera den med hjälp av följande frågor.

### Fråga 1: Handlar utsagan om kunnande?

Exempel: “Vi behöver bli bättre på riskbedömning.”

Detta pekar ofta mot en förmåga. Nästa steg kan vara att fråga vad organisationen behöver kunna göra bättre, på vilken nivå och för vilket syfte.

### Fråga 2: Handlar utsagan om flöde?

Exempel: “Det tar för lång tid från inskickad deklaration till beslut.”

Detta pekar ofta mot en process eller ett värdeflöde. Nästa steg kan vara att beskriva nulägesflödet och hitta var tid, väntan eller omarbete uppstår.

### Fråga 3: Handlar utsagan om utförande?

Exempel: “Handläggarna gör olika när de begär komplettering.”

Detta pekar ofta mot en rutin, instruktion eller regel. Nästa steg kan vara att skilja mellan praktiska arbetssteg och styrande villkor.

### Fråga 4: Handlar utsagan om mottagarens upplevelse eller erbjudande?

Exempel: “Deklaranter behöver bättre digital självservice.”

Detta pekar ofta mot en tjänst, kundresa eller värdeflöde. Nästa steg kan vara att beskriva vad mottagaren behöver kunna göra och vilken nytta tjänsten ska ge.

### Fråga 5: Handlar utsagan om begrepp, data eller beslutunderlag?

Exempel: “Vi menar olika saker med riskindikator.”

Detta pekar ofta mot information, begreppsmodell eller regelbeskrivning. Nästa steg kan vara att definiera begreppet och dess relation till beslut, processer och system.

### Fråga 6: Handlar utsagan om ägarskap eller beslut?

Exempel: “Ingen vet vem som äger regelverkstolkningen.”

Detta pekar ofta mot roller, ansvar och styrning. Nästa steg kan vara att beskriva ansvar för beslut, förvaltning, kvalitet och uppföljning.

## Vanliga misstag

- **Misstag: Att tro att en modelltyp ska lösa alla frågor.**
  - Varför det händer: En organisation har ofta en etablerad mall eller notation som används till allt.
  - Hur du undviker det: Börja med syfte och målgrupp. Välj sedan beskrivningstyp.

- **Misstag: Att kalla allt för process.**
  - Varför det händer: Process är ett välkänt ord och används ofta som samlingsbegrepp.
  - Hur du undviker det: Testa om beskrivningen verkligen handlar om flöde över tid. Om den handlar om kunnande, ansvar eller information behövs kanske en annan beskrivning.

- **Misstag: Att beskriva förmågor som aktiviteter.**
  - Varför det händer: Verb gör beskrivningar konkreta, men kan dra dem mot processnivå.
  - Hur du undviker det: Formulera förmågan som ett stabilt verksamhetskunnande och testa om den är oberoende av nuvarande organisation och system.

- **Misstag: Att fylla processmodellen med rutinens alla detaljer.**
  - Varför det händer: Det känns tryggt att få med allt.
  - Hur du undviker det: Låt processen visa flödet och lägg detaljerade arbetsinstruktioner i separata rutiner.

- **Misstag: Att glömma information och regler.**
  - Varför det händer: Aktiviteter och roller är ofta lättare att se än styrande villkor och informationsbehov.
  - Hur du undviker det: Fråga alltid vilka informationsobjekt och regler som krävs för att processen eller förmågan ska fungera.

## Övningar

### Övning 1: Sortera utsagor

Sortera följande utsagor efter vilken beskrivningstyp de främst pekar mot: förmåga, process, rutin, tjänst, information, regel eller ansvar.

1. “Vi behöver kunna analysera risker tidigare i flödet.”
2. “Det är oklart vem som får besluta om manuell kontroll.”
3. “Deklaranten ska kunna se status digitalt.”
4. “Handläggare registrerar kompletteringar på olika sätt.”
5. “Begreppet kontrollärende används olika i olika system.”
6. “Det tar för lång tid mellan inskickad deklaration och beslut.”
7. “Vi behöver veta när komplettering måste begäras.”

Förslag till svar:

| Utsaga | Primär beskrivningstyp |
|---|---|
| 1 | Förmåga |
| 2 | Ansvar |
| 3 | Tjänst |
| 4 | Rutin |
| 5 | Information |
| 6 | Process eller värdeflöde |
| 7 | Regel |

Det kan finnas flera rimliga svar. Poängen är att formulera varför du väljer en viss typ.

### Övning 2: Beskriv samma situation på tre nivåer

Välj en situation från din egen verksamhet, eller använd “hantera kompletteringsbegäran” från caset.

Beskriv den som:

1. En förmåga.
2. En process.
3. En rutin.

Använd följande stödfrågor:

- Vad behöver organisationen kunna?
- Vilket flöde leder från start till resultat?
- Vilka praktiska steg behöver utföraren följa?

### Övning 3: Hitta fel nivå

Titta på följande beskrivning:

“Riskbedöma deklaration innebär att handläggaren öppnar ärendet, kontrollerar obligatoriska fält, jämför uppgifter mot riskindikatorer, dokumenterar bedömningen, väljer åtgärdskod och skickar ärendet vidare.”

Reflektera:

- Är detta bäst beskrivet som förmåga, process eller rutin?
- Vilka delar hör hemma i en process?
- Vilka delar hör hemma i en rutin?
- Vilka delar kan vara regler eller informationsbehov?

Ett möjligt resonemang är att “riskbedöma deklaration” kan vara en del av en process, medan detaljer som åtgärdskod och systemmoment hör hemma i rutin eller instruktion. Riskindikatorer och obligatoriska fält kan dessutom behöva beskrivas som information och regler.

### Fördjupning

Ta en modell eller beskrivning som redan finns i din organisation. Markera varje del med en enkel etikett:

- F för förmåga.
- P för process.
- R för rutin.
- T för tjänst.
- I för information.
- G för regel.
- A för ansvar.

Om modellen innehåller många etiketter på samma yta kan den behöva delas upp i flera kompletterande beskrivningar.

## Snabb sammanfattning

- Förmågor beskriver vad organisationen behöver kunna.
- Processer beskriver hur arbete skapar resultat över tid.
- Rutiner beskriver hur återkommande arbete utförs i praktiken.
- Tjänster beskriver vad en mottagare erbjuds eller använder.
- Värdeflöden beskriver hur värde skapas från behov till resultat.
- Information beskriver vad verksamheten behöver veta, hantera eller besluta utifrån.
- Regler beskriver villkor som styr beslut och agerande.
- Roller och ansvar beskriver vem som gör, äger, beslutar eller följer upp.
- Samma verklighet kan beskrivas på flera sätt. Syfte och målgrupp avgör vilken beskrivning som är mest användbar.

## Quiz/reflektionsfrågor

1. Vilken fråga svarar en förmåga främst på?
2. Vad är den viktigaste skillnaden mellan process och rutin?
3. När är en tjänstebeskrivning mer användbar än en processbeskrivning?
4. Varför bör regler inte alltid ritas in som processgrenar?
5. Hur kan du avgöra om en modell blandar för många nivåer?
6. Vilken beskrivningstyp skulle du välja om problemet är otydligt ägarskap?
7. Vilken beskrivningstyp skulle du välja om problemet är långa ledtider?

## Nästa steg

Nu finns grundkartan på plats. I nästa kapitel fördjupar vi oss i förmågor: hur de identifieras, namnges, avgränsas och beskrivs utan att glida över i processer, rutiner eller organisationsstruktur.
