# Kapitel 10: Att beskriva så att andra kan använda resultatet

## Varför detta kapitel finns

En verksamhetsbeskrivning är inte klar bara för att den finns på en sida, i ett modelleringsverktyg eller i en presentation. Den är klar först när andra kan förstå vad den betyder, avgöra om den är relevant och använda den i sitt eget arbete.

Det är en viktig skillnad. Många beskrivningar blir aldrig riktigt använda därför att de saknar något grundläggande: ett tydligt syfte, en rimlig nivå, ett begripligt namn, en tydlig avgränsning eller en förklaring av hur de hänger ihop med andra beskrivningar. Resultatet kan se professionellt ut, men ändå vara svårt att använda som beslutsunderlag, kravstöd, förbättringsunderlag eller gemensamt språk.

Det här kapitlet handlar därför om kvalitet i verksamhetsbeskrivningar. Inte kvalitet i betydelsen att modellen är snygg eller följer en viss notation perfekt, utan kvalitet i betydelsen att den fungerar för sitt syfte.

I caset med Tullmyndigheten Atlantis kan beskrivningen “Hantera deklarationer” betyda flera olika saker. Den kan vara en förmåga, en process, en tjänst, en grupp rutiner eller ett helt verksamhetsområde. Om beskrivningen saknar syfte och avgränsning behöver läsaren gissa. En verksamhetsarkitekt kanske tolkar den som en förmåga. En processägare kanske tolkar den som ett flöde. Ett utvecklingsteam kanske tolkar den som ett systemområde. En chef kanske tolkar den som ett ansvar.

Ingen av dessa tolkningar behöver vara fel. Problemet är att beskrivningen inte hjälper dem att förstå vilken tolkning som avses.

En användbar beskrivning behöver därför svara på frågor som:

- Vad beskriver vi?
- Varför beskriver vi det?
- Vem ska använda beskrivningen?
- Vilken nivå ligger den på?
- Vad ingår och vad ingår inte?
- Vilka andra beskrivningar hänger den ihop med?
- Vem äger och förvaltar beskrivningen?
- Hur vet vi om beskrivningen är tillräckligt bra?

Det här kapitlet ger mallar, kvalitetskriterier och praktiska arbetssätt för att besvara dessa frågor.

## Lärandemål

Efter kapitlet ska du kunna:

- formulera verksamhetsbeskrivningar så att syfte, målgrupp och användning blir tydliga
- namnge förmågor, processer, rutiner och andra beskrivningar på ett konsekvent sätt
- ange omfattning, avgränsning, nivå, ägarskap och relationer
- använda enkla mallar för förmågor, processer, rutiner och kompletterande beskrivningar
- bedöma om en beskrivning är tillräckligt bra för sitt syfte
- undvika vanliga kvalitetsproblem som gör beskrivningar svåra att använda

## Innan vi börjar

De tidigare kapitlen har hjälpt dig att skilja mellan olika typer av verksamhetsbeskrivningar och att identifiera kandidater. Nu byter vi fokus från “vad är detta?” till “hur beskriver vi det så att andra kan använda det?”.

Det innebär att vi inte bara tittar på innehållet i själva beskrivningen. Vi tittar också på den metadata och kontext som gör beskrivningen användbar.

Med metadata menas här enkel information om beskrivningen, till exempel:

- namn
- syfte
- målgrupp
- status
- ägare
- källa
- senast uppdaterad
- relationer till andra beskrivningar

Det kan låta administrativt, men i praktiken är det ofta just denna information som avgör om en beskrivning går att lita på. En förmågekarta utan ägare blir snabbt en ögonblicksbild. En process utan start och slut blir svår att förbättra. En rutin utan giltighetsområde blir lätt använd på fel sätt. En ansvarsmatris utan ansvarstyper skapar mer diskussion än klarhet.

En bra verksamhetsbeskrivning behöver alltså både innehåll och sammanhang.

## Grundprincipen: beskrivningens kvalitet avgörs av användningen

Det är frestande att tro att kvalitet handlar om att fylla i så många fält som möjligt. Men en lång mall gör inte automatiskt en beskrivning bättre. Den kan lika gärna göra arbetet tungt, långsamt och svårt att förvalta.

Den viktigaste principen är:

> En verksamhetsbeskrivning är tillräckligt bra när den hjälper rätt målgrupp att fatta rätt beslut eller utföra rätt arbete med rimlig säkerhet.

Det betyder att kvalitet alltid måste bedömas mot användningsområdet.

En beskrivning som ska stödja strategisk prioritering behöver inte innehålla detaljerade arbetssteg. En rutin som ska hjälpa en ny handläggare behöver däremot vara mer konkret. En förmåga som ska användas i portföljstyrning behöver vara stabil och tydligt avgränsad. En process som ska förbättras behöver visa överlämningar, beslutspunkter och resultat. En informationsbeskrivning som ska stödja systemutveckling behöver vara mer precis än en enkel begreppslista i en workshop.

Fråga därför alltid:

- Vilket beslut, vilken dialog eller vilket arbete ska beskrivningen stödja?
- Vad behöver målgruppen förstå för att kunna agera?
- Vilken detaljnivå är tillräcklig?
- Vilken detaljnivå skulle göra beskrivningen onödigt tung?
- Vilka risker uppstår om beskrivningen misstolkas?

I caset med Tullmyndigheten Atlantis kan “Riskbedöma varuflöden” beskrivas på flera nivåer. För ledningen kan en kort förmågebeskrivning räcka. För ett utvecklingsteam kan relationen till informationsobjekt, regler och digitala produkter behöva tydliggöras. För en handläggare räcker inte en förmågebeskrivning alls; där behövs rutiner, instruktioner och beslutstöd.

Samma ämne kräver alltså olika kvalitetsegenskaper beroende på användning.

## En användbar beskrivning har fem grunddelar

Oavsett om du beskriver en förmåga, process, rutin, tjänst, informationsobjekt eller ansvarsfördelning finns det fem grunddelar som nästan alltid behövs.

### 1. Identitet

Beskrivningen behöver ha ett tydligt namn och en tydlig typ.

Exempel:

- Förmåga: Riskbedöma varuflöden
- Process: Genomföra riskbaserad deklarationskontroll
- Rutin: Begära komplettering i deklarationsärende
- Informationsobjekt: Riskindikator
- Roll: Kontrollhandläggare
- Tjänst: Digital tullklarering

Identiteten ska göra det möjligt att hitta, referera till och skilja beskrivningen från andra beskrivningar.

### 2. Syfte

Beskrivningen behöver förklara varför den finns.

Exempel:

> Syftet med processbeskrivningen är att identifiera överlämningar, beslutspunkter och förbättringsmöjligheter i hanteringen av deklarationer som markerats för fördjupad kontroll.

Detta är mer användbart än:

> Syftet är att beskriva processen.

Det senare säger bara vad beskrivningen är. Det säger inte vad den ska användas till.

### 3. Omfattning

Beskrivningen behöver ange vad som ingår och vad som inte ingår.

Exempel:

> Processen börjar när en deklaration har markerats för kontroll och slutar när kontrollresultatet är registrerat och kommunicerat till berörd part. Processen omfattar inte den generella riskmodelleringen eller efterföljande överklagandehantering.

Omfattning är särskilt viktig när flera beskrivningar ligger nära varandra. Utan omfattning börjar de glida in i varandra.

### 4. Innehåll

Beskrivningen behöver innehålla den information som målgruppen faktiskt behöver.

För en förmåga kan det vara definition, resultat, beroenden och mognadsaspekter. För en process kan det vara start, slut, aktiviteter, roller, beslutspunkter och resultat. För en rutin kan det vara steg, ansvar, undantag, kontroller och referenser.

Innehållet ska styras av beskrivningstypen, inte av en allmän önskan att få med allt.

### 5. Förvaltning

Beskrivningen behöver kunna hållas aktuell.

Det innebär minst:

- ägare eller ansvarig roll
- status
- version eller datum
- källa eller beslut
- när den ska ses över
- hur ändringar hanteras

Förvaltning är ofta den del som saknas. Men utan förvaltning blir beskrivningen snabbt osäker. När ingen vet om modellen gäller längre slutar människor använda den eller börjar skapa egna varianter.

## Namngivning: gör skillnaden synlig redan i namnet

Namn är inte bara etiketter. Namn styr hur människor tolkar beskrivningen. Ett otydligt namn gör att beskrivningen kan förstås på flera sätt, även om innehållet senare försöker förklara.

Bra namngivning hjälper läsaren att se skillnaden mellan förmåga, process, rutin, tjänst och informationsobjekt.

### Namn på förmågor

Förmågor bör ofta namnges med ett verb i infinitiv eller en verbfras som uttrycker vad organisationen behöver kunna göra.

Exempel:

- Riskbedöma varuflöden
- Hantera deklarationer
- Tillhandahålla digital självservice
- Förvalta regelverkstolkning
- Kommunicera beslut till berörd part

Ett bra förmågenamn är stabilt över tid. Det bör inte låsa sig vid en viss organisatorisk enhet, ett visst system eller en viss detaljaktivitet.

Mindre bra förmågenamn:

- Riskteamet
- Riskmodulen
- Genomgång av kölistan varje morgon
- Deklarationsprocessen
- Handläggarnas arbetsrutin

Dessa namn pekar snarare på organisation, system, aktivitet, process eller rutin.

### Namn på processer

Processer bör ofta namnges med en verbfras som antyder ett flöde från start till resultat.

Exempel:

- Ta emot och handlägga deklaration
- Genomföra riskbaserad deklarationskontroll
- Begära och hantera komplettering
- Utreda misstänkt avvikelse
- Fatta och kommunicera beslut

Ett bra processnamn bör göra det möjligt att fråga:

- Vad startar processen?
- Vilket resultat skapas?
- Vem eller vad tar emot resultatet?
- Vilka huvudsteg ingår?

Mindre bra processnamn:

- Deklaration
- Kontroll
- Riskbedömning
- Kundservice
- Ärendesystemet

Dessa kan vara områden, förmågor, informationsobjekt eller system, men de visar inte tydligt ett flöde.

### Namn på rutiner och instruktioner

Rutiner och instruktioner bör vara tydliga och konkreta. De får gärna visa vilket moment de stödjer.

Exempel:

- Rutin för kompletteringsbegäran i deklarationsärende
- Instruktion för registrering av kontrollresultat
- Checklista för fullständighetskontroll av deklaration
- Rutin för kvalitetssäkring av beslutsunderlag

Ett bra rutinnamn gör det lätt för användaren att förstå när rutinen ska användas.

Mindre bra rutinnamn:

- Deklarationsarbete
- Handläggning
- Kontroll
- Så gör vi
- Allmän rutin

Dessa namn är för breda för att hjälpa i praktiken.

### Namn på informationsobjekt

Informationsobjekt bör namnges som substantiv eller substantivfraser.

Exempel:

- Deklaration
- Varupost
- Riskindikator
- Kontrollresultat
- Kompletteringsbegäran
- Beslut

Ett informationsobjekt ska inte namnges som en aktivitet. “Riskbedöma deklaration” är inte ett informationsobjekt. “Riskbedömning” kan däremot vara ett informationsobjekt om verksamheten behöver skapa, lagra, använda eller kommunicera en sådan bedömning.

### Namn på roller

Roller bör namnges efter ansvar eller funktion, inte efter person.

Exempel:

- Kontrollhandläggare
- Processägare
- Rutinägare
- Informationsägare
- Beslutsfattare
- Systemförvaltare

Rollnamn bör vara stabila nog att fungera även om organisationen ändras.

## Mall för kort beskrivningskort

Ett praktiskt sätt att öka kvaliteten är att använda ett kort beskrivningskort för varje viktig beskrivning. Det behöver inte vara tungt. Tvärtom bör det vara tillräckligt enkelt för att användas ofta.

| Fält | Fråga att besvara | Exempel |
|---|---|---|
| Namn | Vad heter beskrivningen? | Riskbedöma varuflöden |
| Typ | Vilken sorts beskrivning är det? | Förmåga |
| Syfte | Varför beskriver vi detta? | För att prioritera utveckling av riskanalys och kontrollstöd |
| Målgrupp | Vem ska använda beskrivningen? | Ledning, verksamhetsarkitekter, produktledning |
| Omfattning | Vad ingår? | Bedömning av risk i varuflöden före kontrollbeslut |
| Avgränsning | Vad ingår inte? | Detaljerad rutin för enskild handläggning |
| Nivå | Hur övergripande är beskrivningen? | Förmåga på nivå 2 |
| Relationer | Vad hänger den ihop med? | Processen Genomföra riskbaserad deklarationskontroll |
| Ägare | Vem ansvarar för innehållet? | Förmågeägare eller utsedd verksamhetsansvarig |
| Status | Hur färdig är den? | Utkast, granskad, beslutad |
| Källa | Varifrån kommer informationen? | Workshop, styrdokument, processägare |
| Senast uppdaterad | När uppdaterades den? | 2026-05-19 |

Det viktigaste är inte att exakt dessa fält används överallt. Det viktiga är att varje beskrivning får tillräcklig kontext för att kunna förstås och förvaltas.

## Mall för förmågebeskrivning

En förmågebeskrivning ska hjälpa läsaren förstå vad organisationen behöver kunna göra och varför det är viktigt. Den ska inte bli ett processflöde.

En enkel mall kan innehålla:

| Fält | Innehåll |
|---|---|
| Namn | Kort verbfras, exempelvis Riskbedöma varuflöden |
| Definition | Vad förmågan innebär i verksamheten |
| Syfte | Varför förmågan behövs |
| Resultat | Vilka resultat eller effekter förmågan möjliggör |
| Mottagare eller intressenter | Vem som har nytta av att förmågan fungerar |
| Ingår | Centrala delar av förmågan |
| Ingår inte | Närliggande delar som ska beskrivas separat |
| Beroenden | Processer, information, regler, roller, system eller andra förmågor |
| Mognadsaspekter | Vad som kan bedömas eller förbättras |
| Ägarskap | Vem som ansvarar för förmågebeskrivningen |

Exempel:

| Fält | Exempel |
|---|---|
| Namn | Riskbedöma varuflöden |
| Definition | Förmågan att identifiera, analysera och prioritera risker i varuflöden för att stödja kontroll och beslut |
| Syfte | Ge underlag för effektiv kontroll utan att i onödan fördröja legitima flöden |
| Resultat | Prioriterade risker, riskindikatorer och underlag för kontrollbeslut |
| Mottagare eller intressenter | Kontrollverksamhet, analysfunktion, ledning, digital produktledning |
| Ingår | Riskindikatorer, analysunderlag, prioritering, återkoppling från kontroller |
| Ingår inte | Detaljerad handläggningsrutin för enskild kontroll |
| Beroenden | Deklarationsinformation, regelverk, analysverktyg, kontrollprocesser |
| Mognadsaspekter | Datakvalitet, träffsäkerhet, spårbarhet, återkopplingsförmåga |
| Ägarskap | Utsedd verksamhetsansvarig eller förmågeägare |

Lägg märke till att beskrivningen inte räknar upp steg i ett flöde. Den beskriver vad organisationen behöver kunna och vilka delar som påverkar förmågan.

## Mall för processbeskrivning

En processbeskrivning ska hjälpa läsaren förstå hur arbete går från start till resultat. Den behöver därför ha tydliga gränser och visa hur aktiviteter, roller, beslut och överlämningar hänger ihop.

En enkel mall kan innehålla:

| Fält | Innehåll |
|---|---|
| Namn | Processens namn |
| Syfte | Varför processen beskrivs |
| Startpunkt | Vad som utlöser processen |
| Slutpunkt | När processen är färdig |
| Resultat | Vad processen skapar eller förändrar |
| Mottagare | Vem som behöver resultatet |
| Huvudaktiviteter | De viktigaste stegen på rätt nivå |
| Roller | Vilka roller som medverkar |
| Beslutspunkter | Var flödet kan ta olika väg |
| Överlämningar | Var ansvar eller information lämnas över |
| Information | Viktiga informationsobjekt |
| Regler | Viktiga regler som styr processen |
| Kopplade rutiner | Rutiner eller instruktioner som fördjupar vissa moment |
| Förbättringsfrågor | Vad processen ska analyseras mot |
| Ägarskap | Processägare eller ansvarig funktion |

Exempel:

| Fält | Exempel |
|---|---|
| Namn | Genomföra riskbaserad deklarationskontroll |
| Syfte | Identifiera förbättringsmöjligheter i kontrollflödet och tydliggöra överlämningar |
| Startpunkt | Deklaration har markerats för kontroll |
| Slutpunkt | Kontrollresultat är registrerat och kommunicerat |
| Resultat | Genomförd kontroll och dokumenterat beslut eller åtgärd |
| Mottagare | Deklarant, kontrollverksamhet, uppföljningsfunktion |
| Huvudaktiviteter | Ta emot markering, granska underlag, begära komplettering vid behov, bedöma resultat, fatta beslut, kommunicera utfall |
| Roller | Kontrollhandläggare, beslutsfattare, specialiststöd |
| Beslutspunkter | Komplettering krävs, fysisk kontroll krävs, avvikelse bekräftas |
| Överlämningar | Från riskanalys till kontroll, från handläggare till beslutsfattare |
| Information | Deklaration, riskindikator, kompletteringsbegäran, kontrollresultat |
| Regler | Tillämpade kontrollregler och beslutskriterier |
| Kopplade rutiner | Rutin för kompletteringsbegäran, instruktion för registrering av kontrollresultat |
| Förbättringsfrågor | Ledtid, dubbelarbete, otydliga överlämningar, bristande återkoppling |
| Ägarskap | Processägare för kontrollprocessen |

En processbeskrivning ska inte behöva bära all detalj. Om en aktivitet kräver steg-för-steg-vägledning bör den kopplas till en rutin eller instruktion i stället.

## Mall för rutinbeskrivning

En rutin ska hjälpa någon att utföra ett återkommande arbete på ett tillräckligt enhetligt sätt. Den behöver därför vara mer konkret än en processbeskrivning, men den ska fortfarande vara begriplig och förvaltningsbar.

En enkel mall kan innehålla:

| Fält | Innehåll |
|---|---|
| Namn | Rutinens namn |
| Syfte | Varför rutinen finns |
| När rutinen används | Situation eller trigger |
| Gäller för | Målgrupp, roll eller organisatoriskt område |
| Förutsättningar | Vad som måste finnas innan rutinen används |
| Steg | Praktiska arbetssteg |
| Undantag | Vanliga avvikelser och hur de hanteras |
| Kontroller | Vad som ska kontrolleras innan arbetet är klart |
| System eller verktyg | Om rutinen är kopplad till ett system |
| Kopplad process | Vilken processaktivitet rutinen stödjer |
| Kopplade regler | Vilka regler eller riktlinjer som styr rutinen |
| Ägare | Rutinägare |
| Giltighet | Status, version och datum |

Exempel:

| Fält | Exempel |
|---|---|
| Namn | Rutin för kompletteringsbegäran i deklarationsärende |
| Syfte | Säkerställa att kompletteringar begärs enhetligt, spårbart och med tydlig information till deklaranten |
| När rutinen används | När handläggaren bedömer att underlaget inte räcker för fortsatt prövning |
| Gäller för | Kontrollhandläggare som hanterar deklarationsärenden |
| Förutsättningar | Ärendet är registrerat och brist i underlaget är identifierad |
| Steg | Identifiera saknad information, formulera begäran, registrera begäran, skicka meddelande, bevaka svar |
| Undantag | Akuta ärenden, redan pågående komplettering, otydlig mottagare |
| Kontroller | Begäran är begriplig, tidsfrist anges, ärendet är uppdaterat |
| System eller verktyg | Ärendesystem och meddelandefunktion |
| Kopplad process | Genomföra riskbaserad deklarationskontroll |
| Kopplade regler | Regler för kommunikation, spårbarhet och beslut |
| Ägare | Rutinägare inom kontrollverksamheten |
| Giltighet | Utkast eller beslutad version med datum |

En rutin blir ofta mest användbar när den är skriven för den person som faktiskt ska utföra arbetet. Den ska inte vara så generell att den bara upprepar processen, men inte heller så detaljerad att den måste ändras varje gång ett fält i ett system byter namn.

## Mall för ansvarsfördelning

Ansvarsfördelning bör beskrivas separat när frågan handlar om vem som äger, beslutar, utför, godkänner eller informeras. Om ansvaret göms i löptext eller processpilar blir det ofta otydligt.

En enkel ansvarsmatris kan börja så här:

| Objekt eller aktivitet | Utför | Beslutar | Äger | Bidrar | Informeras |
|---|---|---|---|---|---|
| Uppdatera rutin för kompletteringsbegäran | Rutinägare | Processägare | Kontrollverksamhet | Juridiskt stöd, systemförvaltning | Berörda handläggare |
| Ändra riskindikator | Analysfunktion | Beslutsforum för riskstyrning | Riskförmågeägare | Kontrollverksamhet, IT-stöd | Processägare |
| Fastställa processbeskrivning | Processarkitekt | Processägare | Processägare | Berörda roller | Ledning och utvecklingsteam |

Det viktiga är att ansvarstyperna definieras. “Ansvarig” är ofta för brett. En person kan vara ansvarig för att utföra arbetet, en annan för att fatta beslut, en tredje för att förvalta beskrivningen och en fjärde för att säkerställa att regler följs.

Fråga därför:

- Vem utför?
- Vem beslutar?
- Vem äger helheten?
- Vem behöver bidra?
- Vem behöver informeras?
- Vem ansvarar för att beskrivningen hålls aktuell?

## Relationer: gör kopplingar tydliga men inte överlastade

En beskrivning blir mer användbar när den visar hur den hänger ihop med andra beskrivningar. Men relationer måste hanteras med måtta. Om allt kopplas till allt förlorar modellen sin förklaringskraft.

Börja med de relationer som målgruppen faktiskt behöver.

För en förmåga kan relevanta relationer vara:

- stödjande processer
- digitala produkter
- informationsobjekt
- regler
- mognadsbedömningar
- utvecklingsinitiativ

För en process kan relevanta relationer vara:

- förmågor processen stödjer
- rutiner som fördjupar vissa aktiviteter
- roller som utför eller beslutar
- informationsobjekt som skapas eller används
- systemstöd
- regler som påverkar beslut

För en rutin kan relevanta relationer vara:

- processaktivitet
- roll
- system eller verktyg
- regel eller policy
- checklista eller instruktion
- utbildningsmaterial

Ett praktiskt sätt är att beskriva relationer i en enkel lista:

- Denna rutin stödjer processaktiviteten “Begära komplettering”.
- Processaktiviteten ingår i processen “Genomföra riskbaserad deklarationskontroll”.
- Processen stödjer förmågan “Riskbedöma varuflöden”.
- Rutinen använder informationsobjekten “Deklaration”, “Kompletteringsbegäran” och “Kontrollresultat”.
- Rutinen styrs av regler för kommunikation, tidsfrister och dokumentation.

Detta är ofta mer användbart än en stor bild där alla relationer visas samtidigt.

## Kvalitetskriterier för användbara beskrivningar

Följande kriterier kan användas som checklista vid granskning.

### Tydlighet

Beskrivningen är tydlig när en relevant läsare förstår vad den handlar om utan att behöva gissa.

Frågor:

- Är namnet begripligt?
- Är typen tydlig?
- Finns en kort definition?
- Är centrala begrepp använda konsekvent?
- Går det att se vad beskrivningen inte är?

### Syfteskoppling

Beskrivningen är syfteskopplad när den tydligt stödjer en användning.

Frågor:

- Framgår varför beskrivningen finns?
- Framgår vilken fråga den ska hjälpa till att besvara?
- Är innehållet valt utifrån syftet?
- Saknas något som målgruppen behöver?
- Finns något som bara gör beskrivningen tyngre?

### Rätt nivå

Beskrivningen har rätt nivå när den är varken för övergripande eller för detaljerad för sitt syfte.

Frågor:

- Är nivån lämplig för målgruppen?
- Blandas strategisk nivå med arbetsinstruktioner?
- Har aktiviteter blivit förmågor?
- Har rutindetaljer hamnat i processmodellen?
- Har systemfunktioner blandats ihop med verksamhetsförmågor?

### Avgränsning

Beskrivningen är avgränsad när det framgår vad som ingår och inte ingår.

Frågor:

- Finns start och slut för processer?
- Finns ingår och ingår inte för förmågor och rutiner?
- Är angränsande beskrivningar identifierade?
- Finns tydliga gränser mot organisation, system och ansvar?

### Spårbarhet

Beskrivningen är spårbar när det går att förstå var informationen kommer från och varför den ser ut som den gör.

Frågor:

- Finns källor eller underlag?
- Är viktiga beslut dokumenterade?
- Finns kopplingar till regler, styrdokument eller intervjuer?
- Går det att se vad som är antagande och vad som är beslutat?

### Förvaltningsbarhet

Beskrivningen är förvaltningsbar när den kan hållas aktuell utan orimlig insats.

Frågor:

- Finns ägare?
- Finns status?
- Finns datum eller version?
- Är detaljnivån rimlig att underhålla?
- Finns en tydlig plats där den ska uppdateras?

### Användbarhet

Beskrivningen är användbar när målgruppen faktiskt kan göra något med den.

Frågor:

- Kan den användas i dialog, beslut eller arbete?
- Kan den förklaras för målgruppen på några minuter?
- Hjälper den till att se skillnader, beroenden eller prioriteringar?
- Minskar den missförstånd?
- Leder den till nästa steg?

## Granskningsfrågor för olika beskrivningstyper

Olika beskrivningstyper behöver olika granskningsfrågor.

### Förmåga

- Beskriver namnet vad organisationen behöver kunna göra?
- Är förmågan stabil över tid?
- Är den fri från onödiga process-, system- och organisationsdetaljer?
- Finns tydlig definition?
- Finns relation till mål, värde, processer eller produkter?
- Är nivån konsekvent med andra förmågor?

### Process

- Finns tydlig startpunkt?
- Finns tydlig slutpunkt?
- Finns ett resultat?
- Finns en mottagare?
- Är aktiviteterna på samma nivå?
- Syns beslutspunkter och överlämningar?
- Är rutindetaljer placerade i separata rutiner?

### Rutin

- Framgår när rutinen ska användas?
- Är målgruppen tydlig?
- Är stegen praktiskt användbara?
- Finns undantag och kontroller?
- Är rutinen kopplad till process och regler?
- Är den lagom detaljerad för att kunna förvaltas?

### Information

- Är informationsobjektet tydligt avgränsat?
- Är det beskrivet som information, inte som aktivitet?
- Framgår var informationen skapas, används och förändras?
- Finns relation till processer, regler och system?
- Är definitionen begriplig för verksamheten?

### Regel

- Är regeln formulerad som ett styrande villkor?
- Framgår vad regeln påverkar?
- Finns källa eller mandat?
- Är regeln skild från rutinens praktiska steg?
- Är undantag eller tolkningsbehov tydliga?

### Roll och ansvar

- Är rollen skild från person och organisatorisk enhet?
- Framgår vilket ansvar rollen har?
- Är ansvarstypen tydlig?
- Finns beslut, utförande och ägarskap separerade där det behövs?
- Finns koppling till process, rutin eller förvaltning?

## Status: märk beskrivningen som utkast, granskad eller beslutad

En vanlig orsak till missförstånd är att alla beskrivningar ser lika färdiga ut. En workshopskiss, ett analyserat utkast och en beslutad målbild kan ligga bredvid varandra utan tydlig status. Då börjar människor använda dem på fel sätt.

Använd därför enkel statusmärkning.

| Status | Betydelse | Får användas till |
|---|---|---|
| Idé | Tidig observation eller kandidat | Diskussion och utforskning |
| Utkast | Strukturerad men inte granskad beskrivning | Analys och intern dialog |
| Granskad | Genomgången med relevanta personer | Underlag för planering och förankring |
| Beslutad | Formellt fastställd eller accepterad | Styrning, krav, förvaltning och uppföljning |
| Ersatt | Tidigare version som inte längre gäller | Historik och spårbarhet |

Status ska inte användas för att skapa onödig administration. Den ska användas för att minska risken att fel underlag används i fel sammanhang.

## Dokumentera beslut och osäkerheter

En beskrivning blir mer användbar när den visar vilka beslut som ligger bakom den och vilka frågor som fortfarande är öppna.

Exempel:

| Fråga | Status | Kommentar |
|---|---|---|
| Ska “Riskbedöma varuflöden” vara en egen förmåga eller del av “Styra kontroller”? | Beslutad | Beslutad som egen förmåga eftersom den används i flera processer |
| Ska “Begära komplettering” beskrivas som egen process? | Öppen | Hanteras tills vidare som aktivitet med tillhörande rutin |
| Vem äger rutinen för kompletteringsbegäran? | Öppen | Behöver förankras med kontrollverksamheten |
| Är riskindikator ett informationsobjekt eller en regel? | Delvis beslutad | Riskindikator beskrivs som informationsobjekt; regellogiken beskrivs separat |

Detta är särskilt viktigt i komplexa miljöer där människor annars kan tro att en modell är mer färdig än den är.

## Skriv för mottagaren, inte för modellören

En beskrivning kan vara korrekt men ändå svår att använda. Det händer ofta när den skrivs för den som modellerar snarare än för den som ska förstå den.

Skriv därför med mottagaren i åtanke.

För ledning:

- betona syfte, nytta, beroenden och beslut
- undvik onödiga notationstermer
- visa konsekvenser och prioriteringar

För arkitekter:

- betona struktur, relationer, nivåer och spårbarhet
- visa hur beskrivningen kopplas till andra modeller
- var tydlig med antaganden och avgränsningar

För processägare:

- betona start, slut, resultat, överlämningar och förbättringspunkter
- visa koppling till ansvar och uppföljning
- undvik för teknisk terminologi om den inte behövs

För handläggare eller operativa roller:

- betona konkreta steg, undantag, kontroller och var stöd finns
- skriv tydligt och praktiskt
- undvik övergripande arkitekturspråk i rutiner

För utvecklingsteam:

- betona behov, informationsobjekt, regler, beroenden och beslutspunkter
- visa koppling till digitala produkter och systemstöd
- skilj verksamhetskrav från teknisk lösning

Samma innehåll kan alltså behöva presenteras på olika sätt beroende på målgrupp. Det betyder inte att organisationen ska ha fem olika sanningar. Det betyder att samma grundbeskrivning kan behöva olika vyer.

## Vyer: visa olika delar av samma verklighet

En vy är ett urval av information för en viss målgrupp eller fråga. Vyer är användbara eftersom ingen målgrupp behöver se allt samtidigt.

Exempel på vyer i caset med Tullmyndigheten Atlantis:

- Ledningsvy: förmågor, utvecklingsbehov och strategiska beroenden.
- Processvy: huvudflöden, överlämningar och förbättringspunkter.
- Rutinvyn: praktiska steg och kontroller för handläggare.
- Informationsvy: deklaration, riskindikator, kompletteringsbegäran och kontrollresultat.
- Produktvy: digitala produkter, ansvariga team och koppling till verksamhetsbehov.
- Ansvarsvy: vem som äger, utför, beslutar och informeras.

Vyer minskar behovet av att skapa en enda överlastad modell. De gör det också lättare att återanvända samma grundinformation i flera sammanhang.

## Exempel: från otydlig beskrivning till användbart resultat

Anta att en arbetsgrupp har skrivit följande:

> Kontrollprocessen behöver förbättras. Riskbedömning, kompletteringar och beslut behöver bli tydligare. Systemet ska stödja detta bättre.

Detta är en rimlig start, men den är inte en användbar beskrivning. Den blandar process, förmåga, rutin, beslut, information och systemstöd.

Ett mer användbart resultat kan delas upp så här:

| Typ | Namn | Syfte |
|---|---|---|
| Förmåga | Riskbedöma varuflöden | Förstå vilken förmåga som behöver stärkas för bättre urval och prioritering |
| Process | Genomföra riskbaserad deklarationskontroll | Analysera flöde, överlämningar och beslutspunkter |
| Rutin | Begära komplettering i deklarationsärende | Stödja enhetligt praktiskt arbete |
| Informationsobjekt | Riskindikator | Definiera vilken information som styr urval och uppföljning |
| Regel | Kompletteringsregel | Visa när komplettering ska begäras |
| Roll | Kontrollhandläggare | Klargöra ansvar i processen |
| Digital produkt | Deklarationsportalen | Beskriva vilket systemstöd som påverkas |

Därefter kan varje beskrivning få ett kort beskrivningskort. Resultatet blir mer omfattande än den ursprungliga meningen, men också mycket mer användbart.

## Praktiskt arbetssätt: bygg beskrivningen i tre steg

För att undvika överarbete kan du arbeta i tre steg.

### Steg 1: Skriv minsta användbara beskrivning

Börja med det som behövs för att föra dialog.

För de flesta beskrivningar räcker detta i första steget:

- namn
- typ
- syfte
- målgrupp
- kort definition
- preliminär omfattning
- viktigaste relationer
- öppna frågor

Målet är inte perfektion. Målet är att skapa ett underlag som kan granskas.

### Steg 2: Granska mot syfte och målgrupp

Låt relevanta personer granska beskrivningen.

Fråga:

- Förstår ni vad detta betyder?
- Hjälper det er med den fråga vi försöker besvara?
- Är något fel eller missvisande?
- Är nivån rätt?
- Saknas något för att ni ska kunna använda beskrivningen?
- Finns något som bör flyttas till en annan beskrivning?

Granskningen bör inte bara fråga om beskrivningen är “korrekt”. Den bör fråga om den är användbar.

### Steg 3: Fördjupa bara där det behövs

När beskrivningen är granskad fördjupar du de delar som behövs för användningen.

Exempel:

- Om beskrivningen ska stödja prioritering kan du lägga till mognad, beroenden och utvecklingsbehov.
- Om den ska stödja förbättring kan du lägga till ledtider, överlämningar och problemområden.
- Om den ska stödja rutinändring kan du lägga till steg, undantag och kontroller.
- Om den ska stödja systemutveckling kan du lägga till informationsobjekt, regler och integrationer på rätt nivå.

På så sätt växer beskrivningen med behovet i stället för att bli tung från början.

## Vanliga misstag och kvalitetsproblem

### Problemet: namnet är för brett

Exempel: “Kontroll”.

Varför det händer: Gruppen använder ett vardagsord som alla känner igen.

Konsekvens: Ingen vet om det handlar om förmåga, process, rutin, roll, systemstöd eller verksamhetsområde.

Bättre: “Genomföra riskbaserad deklarationskontroll” som process, “Kontrollhandläggare” som roll och “Kontrollresultat” som informationsobjekt.

### Problemet: syftet saknas

Exempel: “Denna modell beskriver deklarationshantering.”

Varför det händer: Det känns självklart för den som tog fram modellen.

Konsekvens: Modellen används i sammanhang den inte var gjord för.

Bättre: “Modellen används för att identifiera överlämningar och förbättringsmöjligheter i flödet från markerad deklaration till kommunicerat kontrollresultat.”

### Problemet: flera nivåer blandas

Exempel: En processmodell innehåller både huvudsteg, systemklick, regler, rollbeskrivningar och strategiska mål.

Varför det händer: Gruppen försöker få med allt i samma bild.

Konsekvens: Modellen blir svår att läsa och ännu svårare att förvalta.

Bättre: Håll processmodellen på flödesnivå och koppla rutiner, regler, roller och systemstöd som separata beskrivningar.

### Problemet: avgränsningen är implicit

Exempel: Alla i workshopgruppen vet vad som avses, men det står inte i beskrivningen.

Varför det händer: Beskrivningen skapas i en grupp med gemensam bakgrund.

Konsekvens: Nya läsare tolkar beskrivningen annorlunda.

Bättre: Skriv ut start, slut, ingår och ingår inte.

### Problemet: ingen äger beskrivningen

Exempel: En förmågekarta används i flera initiativ men ingen ansvarar för att uppdatera den.

Varför det händer: Modellen skapades som projektleverans.

Konsekvens: Den blir snabbt inaktuell och ersätts av lokala kopior.

Bättre: Ange ägare, status, datum och förvaltningsprincip.

## Övningar

### Övning 1: Förbättra ett namn

Utgå från följande namn:

- Kontroll
- Risk
- Deklaration
- Kundservice
- Komplettering

För varje namn, skapa minst två mer precisa namn:

- ett för en förmåga
- ett för en process, rutin, roll eller informationsobjekt

Exempel:

- “Risk” kan bli förmågan “Riskbedöma varuflöden”.
- “Risk” kan också bli informationsobjektet “Riskindikator”.

Reflektera över hur namnet förändrar tolkningen.

### Övning 2: Skapa ett beskrivningskort

Välj en av följande kandidater:

- Riskbedöma varuflöden
- Genomföra riskbaserad deklarationskontroll
- Rutin för kompletteringsbegäran i deklarationsärende
- Riskindikator
- Kontrollhandläggare

Fyll i ett kort beskrivningskort med:

- namn
- typ
- syfte
- målgrupp
- omfattning
- avgränsning
- relationer
- ägare
- status
- öppna frågor

Målet är inte att skriva perfekt, utan att göra beskrivningen användbar nog för granskning.

### Övning 3: Granska en beskrivning

Granska följande text:

> Deklarationshantering är processen där myndigheten tar emot deklarationer, riskbedömer dem, gör kontroller, använder systemet, kontaktar deklaranter och fattar beslut. Processen ägs av verksamheten och ska stödja digitalisering.

Besvara:

1. Vilka begrepp blandas ihop?
2. Vilken typ av beskrivning verkar texten försöka vara?
3. Vad behöver avgränsas?
4. Vilka separata beskrivningar skulle behövas?
5. Hur skulle du skriva om syftet?

### Fördjupning

Välj en verklig verksamhetsbeskrivning från din egen organisation. Granska den med kvalitetskriterierna i kapitlet:

- tydlighet
- syfteskoppling
- rätt nivå
- avgränsning
- spårbarhet
- förvaltningsbarhet
- användbarhet

Skriv sedan tre förbättringar som skulle göra beskrivningen lättare att använda.

## Snabb sammanfattning

- En verksamhetsbeskrivning är användbar först när rätt målgrupp kan förstå och använda den.
- Kvalitet avgörs av användningen, inte av hur många fält som fyllts i.
- De flesta beskrivningar behöver identitet, syfte, omfattning, innehåll och förvaltning.
- Namngivning är ett av de enklaste sätten att göra skillnaden mellan förmåga, process, rutin, information och roll tydlig.
- Beskrivningskort hjälper till att skapa kontext utan att arbetet blir för tungt.
- Förmågor, processer och rutiner behöver olika mallar eftersom de svarar på olika frågor.
- Relationer ska vara tydliga men inte överlastade.
- Status, ägarskap och källor minskar risken att beskrivningar misstolkas eller blir inaktuella.
- Vyer gör det möjligt att visa olika delar av samma grundinformation för olika målgrupper.

## Quiz/reflektionsfrågor

1. Varför räcker det inte att en verksamhetsbeskrivning är korrekt?
2. Vilka fem grunddelar bör de flesta verksamhetsbeskrivningar ha?
3. Vad är skillnaden mellan syfte och omfattning?
4. Varför är namngivning särskilt viktig när man skiljer mellan förmågor, processer och rutiner?
5. När bör en processbeskrivning hänvisa till en rutin i stället för att själv innehålla alla detaljer?
6. Vad är risken med att sakna statusmärkning på modeller och beskrivningar?
7. Hur kan vyer hjälpa olika målgrupper utan att organisationen får flera konkurrerande sanningar?
8. Vilka kvalitetskriterier skulle du använda först om du snabbt behövde granska en modell?

## Nästa steg

Nu har vi gått igenom hur beskrivningar kan göras användbara: hur de namnges, avgränsas, förses med syfte, kopplas till andra beskrivningar och förvaltas över tid.

Nästa kapitel samlar de vanligaste misstagen. Där använder vi begreppen från hela boken för att se varför förmågor blir aktiviteter, varför processer blir organisationsscheman, varför rutiner blir för generella och varför modeller ibland blir mer imponerande än användbara.
