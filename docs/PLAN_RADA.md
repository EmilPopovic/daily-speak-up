# Plan rada i model suradnje

Ovaj dokument opisuje plan rada i organizaciju grupe tijekom razvoja projekta. Svrha dokumenta je da služi članovima grupe kao podsjetnik na sve sastavnice modela suradnje, te s njime upoznati asistente i profesore.

Ovo je high-level model kojeg se trudimo držati tijekom cijelog projekta - od razrade specifikacije, preko razvoja aplikacije, sve do testiranja i konačnog puštanja u pogon.

## Osnovna ideja

Osnovna ideja modela suradnje temeljena je na slijedu dvotjednih ciklusa. Ciklus započinje i završava Općim Sastankom svih članova grupe, u fiksno vrijeme svaki četvrtak. Četvrtkom u sredini ciklusa održava se Pregledni Sastanak. Ti se sastanci u pravilu održavaju uživo, u prostoriji na FER-u.

Svaki se dan na Discordu održava asinkroni standup - gdje svatko piše što je radio jučer, što planira raditi danas te ima li ikakvih problema.

### Opći Sastanak

Opći Sastanak je temelj modela - na njemu se određuje na čemu će se raditi u sljedećem dvotjednom ciklusu, određuju se zadaci, raspodjeljuju uloge i definiraju rokovi. Svi članovi grupe trebaju biti prisutni na Općem Sastanku. Sastanak vodi voditelj grupe prateći dnevni red koji je dan ranije poslao ostalim članovima. Tijekom sastanka jedan član grupe vodi zapisnik.

Na temelju zapisnika se otvaraju Issues na GitHubu i dodijeljuju članovima. Cilja se na to da je za svaki zadatak odgovorno dvoje do troje članova. To su uglavnom high-level zadaci koje odgovorni članovi trebaju razraditi na Tehničkim Sastancima (npr. na Discordu).

Ciljevi Općeg Sastanka temeljeni su na očekivanim tjednim akcijama na stranici predmeta.

### Pregledni Sastanak

Pregledni Sastanak održava se tjedan dana nakon Općeg Sastanka. Cilj tog sastanka je napraviti pregled napretka na zadacima određenim na prošlotjednom sastanku, raščistiti eventualne nedoumice te, ako je potrebno, redefinirati ili dodati nove zadatke. Planira se finaliziranje zadataka te predaja na konačni review nakon kojeg slijedi puštanje u produkciju.

### Definition of Done za ciklus

Ciklus se smatra završenim kada su ispunjeni sljedeći uvjeti:

- Svi zadaci iz sprint backlog-a su završeni ili prebačeni u sljedeći ciklus
- Kod je pregledan i odobren
- Promjene su dokumentirane na Wiki-ju
- Google Sheets tablica je ažurirana stvarnim utrošenim satima
- Retrospektiva je provedena i akcijske točke su dokumentirane

## Komunikacija

Za internu komunikaciju koriste se WhatsApp i Discord. WhatsApp služi za brze dogovore ili hitne obavijesti, dok se sve tehničke diskusije događaju u zasebnim kanalima Discord servera (npr. `#backend`, `#testiranje`...).

## Praćenje rada

Za praćenje i organiziranje rada većinski se koriste dvije platforme - GitHub projekt i Google Sheets.

### GitHub Issues

Svaka promjena na repozitoriju mora imati pripadni Issue napisan po jednom od predložaka. Postoje predlošci za dodavanje funkcionalnosti, prijavu buga, nadopunjavanje dokumentacije, zahtjev za testiranje, te zakazan sastanak.

Svaki Issue ima detaljno razrađen opis, tag i uvjete zatvaranja (Definition of Done). Otvoren Issue automatski je dodan u GitHub projekt koristeći Workflow.

### GitHub projekt

GitHub projekt baziran je na Kanban pregledu Issue-a i Pull Requestova. Zadaci su razvrstani između `Backlog`, `Ready`, `In progress`, `In review`, `Done`, `Meeting`. Ovakva organizacija omogućuje lak pregled trenutnih i budućih aktivnosti.

### Google Sheets

Svaki se zadatak prati i u Google Sheets tablici. Za svaki se zadatak dodaje novi redak tablice, za članove upisuje uloga u zadatku (`Vodi`, `Sudjeluje`, `Review`, `Informiran`), te koliko je vremena utrošeno na pojedini zadatak.

### GitHub Wiki

Sva projektna dokumentacija (specifikacija zahtjeva, arhitektura, dijagrami) održava se na GitHub Wikiju. Wiki se ažurira kontinuirano tijekom ciklusa, a finalizira na kraju svakog ciklusa.

## Promjene koda

Repozitorij ima četiri glavne grane - `main`, `test`, `dev`, `devdoc`.

Sadržaj grane `main` automatski je deployan na poslužitelj. `main` je zaštićena grana - na nju nije moguće napraviti push (već samo pull request), te svaki pull request mora dobiti jedno odobrenje od člana s administratorskim pravima. Administartori repozitorija su E. Popović i M. Jurasić.

Sadržaj grane `test` također se automatski šalje na poslužitelj, ali u orkuženje za testiranje. Budući da to okruženje nije produkcijsko, grana nije zaštićena.

Za svaki feature otvara se nova grana od grane `dev`, te se mergea nazad na granu `dev`. Ako se ne radi o promjeni koda, već o promjeni dokumentacije, koristi se grana `devdoc`.

To znači da promjene napravljene na grani feature prvo idu na granu `dev`, nakon toga na granu `test`, a tek nakon što je utvrđeno da cijeli sustav radi ispravno na toj grani, može se pustiti u produkciju na grani `main`.

Odluku o puštanju u produkciju donose administratori nakon automatiziranog i ručnog testiranja u okruženju koje je jednako produkcijskom.
