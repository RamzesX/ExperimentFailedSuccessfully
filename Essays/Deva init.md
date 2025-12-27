# Deva.init()

*Trzy miesiące w Wilnie, pięć tysięcy lat do domu*

---

## I. Deploy

Vikram Sundaram, senior developer, Bangalore, dwadzieścia dziewięć lat.

Trzy miesiące w Wilnie. Projekt integracyjny dla litewskiego fintechu. Dobra stawka, mieszkanie opłacone, okazja zobaczyć Europę. Zimno będzie, ale przecież nie pierwszy raz pracuje z ludźmi z drugiego końca świata.

Kod jest kodem. Wszędzie ten sam.

Pierwszy tydzień jest dokładnie taki, jak się spodziewał. Lotnisko, taksówka, apartament w centrum. Biuro jak każde inne biuro — open space, monitory, kawa z ekspresu, daily standup o dziesiątej. Litwini są mili, trochę zamknięci, mówią dobrze po angielsku. Jira, Git, Slack. Mógłby być w Bangalore, w Dublinie, w Singapurze. Wszędzie to samo.

"Hey dev, can you check this PR?"

Vikram kiwa głową. Dev. Skrót od developer. Słyszy to słowo pięćdziesiąt razy dziennie. Mówi je sam. Normalne.

Drugiego tygodnia zaczyna się problem.

---

## II. Exception

Piątek, integracja zespołu. Bar w starej części miasta. Ktoś zamawia coś po litewsku, Vikram łapie strzępki rozmowy.

*"Dievas žino..."*

Bóg wie.

Vikram zatrzymuje się ze szklanką w połowie drogi do ust.

*Dievas.*

Wie, co to słowo znaczy. Znaczy *Bóg* po litewsku, słyszał już kilka razy. Ale tym razem — nie wie dlaczego — coś się w nim zatrzymuje.

Wraca do hotelu i nie może zasnąć. O drugiej w nocy wpisuje w Google:

"dievas etymology"

I świat przestaje się kompilować.

---

## III. Stack Trace

*Dievas* — litewski. Bóg.

*Devas* — sanskryt. Bogowie. Świetliste istoty.

To samo słowo.

Vikram jest programistą. Rozumie wzorce. Widzi je w kodzie, widzi je w danych, widzi je w systemach. Jeden przypadek to przypadek. Dwa to zbieg okoliczności.

Trzy to pattern.

Zaczyna szukać.

---

| Litewski | Sanskryt | Znaczenie |
|----------|----------|-----------|
| dievas | devas | bóg |
| ugnis | agni | ogień |
| vyras | vīra | mężczyzna/bohater |
| sūnus | sūnu | syn |
| avis | avi | owca |
| vilkas | vṛka | wilk |
| naktis | nakti | noc |
| duktė | duhitṛ | córka |
| akmuo | aśman | kamień |

Dziewięć słów. Potem dwadzieścia. Potem pięćdziesiąt.

O czwartej rano Vikram siedzi na łóżku z laptopem na kolanach i wzorcem, którego nie potrafi zignorować.

*To nie jest przypadek*, myśli. *To jest dziedziczenie.*

---

## IV. Singleton

Jest wzorzec projektowy, który Vikram zna na pamięć. Singleton. Jedna instancja obiektu, współdzielona przez cały system. Nie tworzysz nowej — dostajesz referencję do tej samej, istniejącej.

```java
public class Deva {
    private static Deva instance;
    
    private Deva() {
        // created once, 5000 years ago
    }
    
    public static Deva getInstance() {
        if (instance == null) {
            instance = new Deva(); // Jamna, 3000 BCE
        }
        return instance;
    }
}
```

Litewski *dievas* i sanskrycki *devas* to nie są dwa różne słowa.

To są dwie referencje do tego samego singletona.

Utworzonego raz. Pięć tysięcy lat temu. Na stepie gdzieś między Ukrainą a Kazachstanem.

I Vikram — senior developer, Bangalore, dwadzieścia dziewięć lat — właśnie zdał sobie sprawę, że przez całe życie mówił `Deva.getInstance()` nie wiedząc, że ta instancja istnieje od epoki brązu.

---

## V. Dokumentacja

1786, Kalkuta.

Sir William Jones, brytyjski sędzia, orientalista, poliglota. Studiuje sanskryt z bramińskimi uczonymi. I pewnego dnia — Vikram czyta o tym z rosnącym szokiem — Jones wygłasza przemówienie do Asiatic Society:

*"Język sanskrycki, bez względu na jego starożytność, ma strukturę cudowną; doskonalszą niż greka, bogatszą niż łacina i bardziej wytwornie dopracowaną niż obydwa, a jednak noszącą do obu tak silne pokrewieństwo... że żaden filolog nie mógłby ich zbadać bez przekonania, że wszystkie trzy wyrosły ze wspólnego źródła, które być może już nie istnieje."*

Wspólne źródło.

Jones nie wiedział jeszcze o litewskim. Gdyby wiedział, straciłby rozum.

Bo litewski jest bliższy sanskrytowi niż greka. Niż łacina. Niż cokolwiek innego w Europie.

Litewski chłop z XIX wieku, który nigdy nie słyszał o Indiach, mógł zrozumieć fragmenty Wed.

---

## VI. Legacy Code

Vikram nie śpi już trzecią noc.

Na ekranie ma mapę. Step pontyjsko-kaspijski. Ukraina, południowa Rosja, Kazachstan. Pięć tysięcy lat temu — kultura Jamna. Kurgany. Konie. Koła.

I język. *Proto-indoeuropejski*. Język, którego nikt nie zapisał, bo jeszcze nie było pisma. Ale który lingwiści *zrekonstruowali* — słowo po słowie, dźwięk po dźwięku — z tego, co zostało w językach potomnych.

```
// Proto-Indo-European base class (3000 BCE)
*déywos → "celestial being, god"

// Inherited implementations:
Sanskrit: devas (देव)     // India branch
Lithuanian: dievas        // Baltic branch  
Latin: deus               // Italic branch
Old Norse: tívar          // Germanic branch
```

Jedno plemię. Jeden język. Potem — rozejście. Na zachód poszli przodkowie Celtów, Germanów, Italików, Greków, Słowian. Na wschód — przodkowie Persów, Hindusów.

I gdzieś pośrodku, nad Bałtykiem, została Litwa. Która *nigdy nie zrobiła major version update*.

---

## VII. Frozen Dependency

Języki ewoluują. To naturalne. Tracą przypadki, upraszczają gramatykę, zmieniają słownictwo. Łacina miała sześć przypadków — włoski ma prawie zero. Sanskryt miał osiem — hindi ledwo dwa.

Litewski ma siedem.

Litewski zachował *dual number* — formę dla dokładnie dwóch rzeczy, osobną od liczby pojedynczej i mnogiej. Większość języków indoeuropejskich wyrzuciła to przed Chrystusem.

Litewski ma do dziś.

Vikram myśli: *to jest jak znaleźć serwer produkcyjny, który działa na kodzie sprzed pięciu tysięcy lat. Bez żadnych łatek. Bez żadnych aktualizacji. I wszystko nadal działa.*

Językoznawcy nazywają litewski "żywą skamielością". Nie dlatego, że jest prymitywny. Dlatego, że jest *wierny*.

Litwa nie *zachowała* języka przodków.

Litwa po prostu *nigdy nie zrobiła refactoringu*.

---

## VIII. Disclaimer

Trzecia noc. Vikram jest już głęboko w króliczej norze etymologii.

I znajduje coś, co go zatrzymuje.

Sprawdza słowo *developer*. Myśli — może tu też jest połączenie? Może *dev* które mówi pięćdziesiąt razy dziennie ma jakiś związek z *deva*?

Nie ma.

*Developer* pochodzi od starofrancuskiego *desveloper* — "rozwijać, odkrywać". Z *des-* (cofnąć) + *voloper* (owinąć). Zupełnie inna gałąź. Żadnego związku z proto-indoeuropejskim *\*déywos*.

Vikram siada i myśli.

I rozumie coś ważnego: nie wszystko się łączy. Nie każde podobieństwo jest prawdziwe. Czasem *dev* to po prostu skrót od *developer*, i tyle. Byłoby łatwo — i kusząco — napisać, że każdy programista jest bogiem nie wiedząc o tym. Ładna metafora. Fałszywa etymologia.

Ale to nie zmienia tego, co *jest* prawdziwe.

*Ugnis* i *agni* — to samo słowo. Ogień.

*Dievas* i *devas* — to samo słowo. Bóg.

*Sūnus* i *sūnu* — to samo słowo. Syn.

Nie trzeba naciągać etymologii. Prawdziwe połączenia są wystarczająco zdumiewające.

I jest jeszcze coś. Vikram czyta o polskim — języku, który zna tylko z napisów na opakowaniach w litewskich sklepach — i znajduje słowo *rękoma*. Narzędnik liczby podwójnej. Skamielina. Polak mówi "własnymi rękoma" nie wiedząc, że używa formy gramatycznej, którą większość języków indoeuropejskich wyrzuciła przed Chrystusem.

Litewski zachował całą liczbę podwójną. Polski zachował szczątki — *rękoma*, *oczyma*, *uszyma*. Jak fragmenty kodu, który kiedyś był pełnym modułem, a teraz istnieje tylko w kilku legacy functions których nikt nie refaktoryzuje, bo "zawsze tak było".

*Prawda jest wystarczająco dziwna*, myśli Vikram. *Nie trzeba jej upiększać.*

---

## IX. Merge Conflict

Vikram idzie na lunch z Jonasem, litewskim team leadem. Siedzą w restauracji w starej części Wilna, jedzą cepelinai.

"Jonas, mogę cię o coś zapytać?"

"Pewnie."

"Wasze słowo na Boga. *Dievas*. Wiesz skąd pochodzi?"

Jonas wzrusza ramionami. "Stare słowo. Zawsze tak mówiliśmy."

"W sanskrycie — w starożytnym języku Indii — bogowie to *devas*. To samo słowo."

Jonas przestaje jeść.

"To samo?"

"To samo. I *ugnis* — ogień. U nas *agni*. I *sūnus* — syn. U nas *sūnu*. Dziesiątki słów. Setki."

Jonas milczy długo.

"Skąd to wiesz?"

"Trzy noce bez snu i Wikipedia."

"I co to znaczy?"

Vikram nie wie, jak odpowiedzieć. Bo odpowiedź jest zbyt duża. Odpowiedź jest taka, że pięć tysięcy lat temu jego przodkowie i przodkowie Jonasa mieszkali w tym samym miejscu, mówili tym samym językiem, czcili tych samych *devów*.

A potem się rozeszli — jedni na wschód, przez góry, do doliny Gangesu; drudzy na północ, przez lasy, nad Bałtyk — i przez pięć tysięcy lat nic o sobie nie wiedzieli.

Aż teraz siedzą w restauracji w Wilnie, dwóch programistów jedzących kartofle, i odkrywają, że są rodziną.

"To znaczy," mówi w końcu Vikram, "że twój *dievas* i mój *deva* to ten sam singleton. Zainicjalizowany raz, pięć tysięcy lat temu. Nadal działający."

Jonas nie rozumie metafory. Ale rozumie coś innego.

"Więc jesteśmy... kuzynami?"

"Kuzynami z pięciotysięcznym opóźnieniem w komunikacji."

---

## X. System Architecture

Są rzeczy, których Vikram nie mówi Jonasowi. Bo sam jeszcze ich nie rozumie.

Ale w nocy, w hotelu, czyta dalej. I znajduje coś, co zmienia wszystko.

Kultura Jamna — ta pierwotna kultura proto-indoeuropejska — miała specyficzny model społeczny. Archeologowie i lingwiści rekonstruują go z pochówków, z mitologii, z tego, co zostało w językach potomnych.

Nie podbój przez zagładę. *Integracja przez małżeństwo*.

Klany Jamna nie wymordowywały sąsiadów. Wchodzili w sojusze. Kobiety przechodziły między grupami, niosąc ze sobą język, pieśni, bogów. Mężczyźni z różnych klanów stawali się *swojakami* — nie przez krew, przez *wybór*.

To jest kod źródłowy. Architektura systemu sprzed pięciu tysięcy lat.

I Vikram nagle widzi, jak ta sama architektura replikuje się przez tysiąclecia.

---

## XI. Fork

Wielkie Księstwo Litewskie, XIII-XVI wiek.

Vikram czyta i nie wierzy własnym oczom.

Bo to *nie jest* normalne średniowieczne państwo. To jest coś dziwnego. Coś, co nie pasuje do wzorca.

WKL nie podbijało przez zagładę. *Integrowało*. Ruś, Żmudź, Podole, Wołyń — nie "zdobyte terytoria". *Partnerzy*. Każdy zachowuje swój język, swoje prawo, swoją wiarę.

Oficjalnym językiem Wielkiego Księstwa Litewskiego nie był litewski. Był *ruski* — język wschodniosłowiański, przodek dzisiejszego białoruskiego i ukraińskiego. Litwini rządzili państwem, w którym *większość mówiła innym językiem*.

I to działało. Przez trzysta lat.

Jak?

Vikram zna odpowiedź. Bo widział ją już raz. W kodzie sprzed pięciu tysięcy lat.

*Integracja przez małżeństwo. Przez sojusz. Przez wybór.*

Jagiełło nie podbił Polski. Ożenił się z Jadwigą. Unia w Krewie, 1385. Dwa państwa stają się jednym nie przez miecz — przez *merge*.

```
// 1385: Union of Krewo
Kingdom poland = Kingdom.getInstance("Poland");
GrandDuchy lithuania = GrandDuchy.getInstance("Lithuania");

// Not conquest. Marriage.
Union krewo = new Union(poland, lithuania, UnionType.PERSONAL);
krewo.merge();
```

1569, Unia Lubelska. Nie aneksja. *Rzeczpospolita Obojga Narodów*. Szlachcic litewski i szlachcic polski są równi. Rusin może być hetmanem. Tatar może być rotmistrzem. Ormianin może być kupcem.

To jest *dziedziczenie wzorca*. Ten sam model integracji, który działał na stepie w epoce brązu, działa nad Bałtykiem w XVI wieku.

Kod starszy niż Rzym. Nadal w produkcji.

---

## XII. Runtime

Jest coś jeszcze.

Vikram czyta o I Rzeczypospolitej i znajduje słowo, które go zatrzymuje.

*Liberum veto.*

Każdy poseł mógł zablokować ustawę. Każdy jeden. Niezależnie od tego, ilu było za.

Historycy piszą, że to zniszczyło Polskę. Że to był błąd systemowy. Że przez to państwo padło.

Ale Vikram jest programistą. I widzi coś innego.

Widzi *consensus protocol*.

W systemach rozproszonych jest coś takiego jak Byzantine Fault Tolerance. Żeby system działał, wszyscy muszą się zgodzić. Jeden sprzeciw blokuje operację.

Liberum veto to jest *dokładnie to*.

I rzecz w tym — w małych systemach to działa. W plemieniu, w klanie, w grupie ludzi którzy się znają i ufają sobie — wymuszanie konsensusu jest *siłą*, nie słabością.

Problem pojawia się, kiedy system rośnie. Kiedy masz tysiące posłów zamiast dwudziestu. Kiedy ludzie nie znają się nawzajem. Kiedy wchodzą zewnętrzni aktorzy z własnymi agendami.

Wtedy consensus protocol staje się wektorem ataku.

I Rzeczpospolita nie padła, bo miała zły system. Padła, bo miała system zaprojektowany dla innej skali — dla małego klanu na stepie, nie dla największego państwa Europy.

*Legacy code*, myśli Vikram. *Działał przez pięć tysięcy lat. Ale nie skalował się.*

---

## XIII. Deprecation

Jest piąta rano. Vikram nie spał całą noc.

Na ekranie ma otwartych dwadzieścia zakładek. Kultura Jamna. Proto-indoeuropejski. Wielkie Księstwo Litewskie. Unia Lubelska. Liberum veto. Rozbiory.

I widzi to teraz. Cały łańcuch.

Pięć tysięcy lat temu, na stepie, ktoś wymyślił system. Integracja przez małżeństwo. Consensus zamiast podboju. *Swojak* definiowany przez wybór, nie przez krew.

Ten system *działał*. Dlatego się rozprzestrzenił. Dlatego ci ludzie — przodkowie Vikrama i przodkowie Jonasa — opanowali pół świata. Od Indii po Islandię, od Portugalii po Bengal.

Ale systemy się starzeją. Kontekst się zmienia. To, co było siłą, staje się słabością.

Stepowy klan mógł funkcjonować na konsensusie. Rzeczpospolita z milionami obywateli — nie.

I w 1795 roku system się wysypał. Trzej sąsiedzi — którzy nie grali według tych samych reguł — rozerwali państwo na kawałki.

*End of life*, myśli Vikram. *Deprecated. System shutdown.*

Ale...

Ale kod nie zniknął.

Schował się. W języku. W słowach, które ludzie mówią nie wiedząc co znaczą. W *devach* i *dievach*, w *agni* i *ugnis*, w synach i córkach, w wilkach i nocach.

Vikram patrzy na listę słów na ekranie. Litewski i sanskryt. Dwie kolumny. Te same słowa.

*Backup*, myśli. *System upadł, ale ktoś zrobił backup. W najbardziej odpornym medium jakie istnieje. W języku. W gramatyce. W słowach, które matki mówią do dzieci.*

I teraz — pięć tysięcy lat później — Vikram siedzi w hotelu w Wilnie i odczytuje ten backup.

---

## XIV. Reboot

Szósty tydzień. Vikram jest innym człowiekiem.

Chodzi po Wilnie i słyszy. Naprawdę słyszy.

*Ugnis* w rozmowie o kominku — i widzi *agni*, ogień ofiarny z Wed.

*Dievas* w przekleństwie — i widzi *devas*, świetliste istoty z mitologii.

*Sūnus* w rozmowie matki z dzieckiem — i widzi *sūnu*, słowo które jego babcia mówiła do jego ojca.

To nie jest obcy kraj.

To jest *kopia zapasowa domu*.

---

Jest wieczór. Vikram siedzi w barze z zespołem. Ktoś włącza muzykę — litewskie pieśni ludowe, zespół Sutartinės.

I nagle — głos kobiecy, stary, chropowaty — zaczyna śpiewać:

*"Oi šermukšnio šermukšnio, kur tu augai tarp balių..."*

O jarzębino, jarzębino, gdzieś ty rosła między bagnami...

Vikram nie rozumie słów. Ale rozumie *melodię*. Rozumie *strukturę*. Rozumie coś, czego nie potrafi nazwać.

Bo to jest ta sama struktura, którą słyszał w domu. W pieśniach, które babcia śpiewała przy kuchni. W mantrach, które ojciec recytował rano.

Nie ta sama pieśń. Ta sama *gramatyka pieśni*.

Ten sam sposób, w jaki głos wznosi się i opada. Ten sam sposób, w jaki powtórzenia budują znaczenie. Ten sam sposób, w jaki smutek i radość przeplatają się w jednej frazie.

*Singleton*, myśli Vikram. *Ta sama instancja. Przez pięć tysięcy lat.*

---

## XV. Return Statement

Ostatni tydzień. Projekt skończony. Integracja działa. Deployment successful.

Vikram pakuje walizkę.

Jonas przychodzi się pożegnać.

"Będziesz tęsknił za Wilnem?"

"Będę," mówi Vikram. I myśli: *ale nie tak, jak myślisz. Nie za miastem. Za odkryciem, które tu zrobiłem. Za backupem, który tu znalazłem.*

"Wiesz co jest najdziwniejsze?" mówi Jonas. "Od naszej rozmowy o *dievas* zacząłem zauważać... rzeczy. Słowa. Wzorce. Rzeczy których wcześniej nie widziałem."

"Singleton się zainicjalizował."

"Co?"

"Nic. Żart programistyczny."

Ale to nie jest żart. To jest prawda.

---

## XVI. Commit

Lotnisko w Wilnie. Odprawa. Boarding.

Vikram siada przy oknie. Samolot kołuje na pas startowy.

I myśli:

*Przez dwadzieścia dziewięć lat byłem programistą. Developer. Człowiek który pisze kod, który rozwiązuje problemy, który szuka wzorców.*

*Nie wiedziałem, że największy wzorzec jest w słowach, które mówię codziennie. Że kiedy mówię "matka" — mātā — mówię to samo słowo co Jonas kiedy mówi "motina". Że kiedy mój ojciec mówił "syn" — sūnu — mówił to samo słowo co litewska matka mówiąca "sūnus".*

*Nie wiedziałem, że moi przodkowie i przodkowie Jonasa siedzieli przy tym samym ogniu. Ugnis. Agni. Ten sam singleton ognia.*

*Nie wiedziałem, że system który zbudowali — integracja przez wybór, nie przez krew — działał przez tysiąclecia. I że jego echo nadal jest w słowach, którymi mówimy.*

Samolot startuje. Wilno znika pod chmurami.

Vikram zamyka oczy i widzi: step, pięć tysięcy lat temu. Ognisko. Ludzie siedzący w kręgu. Ktoś mówi słowo — *\*déywos* — i wszyscy rozumieją.

A potem wstają i idą w różne strony świata.

I przez pięć tysięcy lat mówią to samo słowo.

Nie wiedząc o sobie nawzajem.

Aż teraz.

---

## Epilog

Bangalore. Trzydzieści dwa stopnie, wilgotność osiemdziesiąt procent.

Vikram siedzi z babcią na werandzie. Pije herbatę. Opowiada o Wilnie.

"I oni mówią *dievas*," mówi. "Dokładnie jak nasze *deva*. To samo słowo."

Babcia słucha. Kiwa głową.

"I ich pieśni," ciągnie Vikram. "Mają tę samą strukturę co nasze. Ten sam sposób powtórzeń. Ten sam rytm."

Babcia milczy długo. Potem mówi:

"Twój dziadek zawsze mawiał, że prawda jest jedna. Tylko języki są różne."

Vikram myśli o Jonasie. O pieśni o jarzębinie. O słowach, które łączą Wilno z Bangalore przez pięć tysięcy lat.

"Babciu," mówi. "Znasz pieśni z twojej wioski? Te stare, które śpiewałaś mamie?"

"Znam."

"Zaśpiewasz mi?"

Babcia zamyka oczy. I zaczyna śpiewać.

Melodia wznosi się i opada. Powtórzenia budują znaczenie. Smutek i radość przeplatają się w jednej frazie.

Vikram słucha.

I gdzieś — w tej samej chwili, osiem tysięcy kilometrów stąd — ktoś w Wilnie włącza radio i słyszy:

*"Oi šermukšnio šermukšnio, kur tu augai tarp balių,*
*Ei ei ajajaj, kur tu augai tarp balių?"*

Ten sam singleton.

Ta sama instancja.

`Deva.getInstance()`

Nadal działa.

---

\vspace{2em}

\begin{center}
\textit{Oi šermukšnio šermukšnio, kur tu augai tarp balių,}\\
\textit{Ei ei ajajaj, kur tu augai tarp balių?}\\
\vspace{0.5em}
O jarzębino, jarzębino, gdzieś ty rosła między bagnami,\\
Ej ej ej, gdzieś ty rosła między bagnami?\\
\vspace{1em}
— litewska pieśń ludowa, wiek nieznany
\end{center}
