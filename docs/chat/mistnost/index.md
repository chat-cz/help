# Místnost

Místnost je klasicky rozdělena na tři části. Hlavní plocha s texty, dole je řádek na psaní a vpravo seznam uživatelů.

## Zobrazení textů

Největší část obrazovky. Zobrazují se buď systémové hlašení (malé šedé písmo – např. o vstupu do místnosti, reakce na lomítkové příkazy apod.) nebo texty od uživatelů. Na začátku řádku je nick autora. Pokud se jedná o šeptání, je označeno šipkou (od koho⇛komu).

Po najetí kurzorem na text se zobrazí menu s časem zprávy a několika ikonami:
otevřít nové okno s šeptáním, ignorace, smazat ten konkrétní řádek

## Seznam uživatelů

V pravém sloupci je seznam uživatelů v místnosti. Každý řádek začíná nickem a následuje několik ikonek:

– nastavení ignorace (ignorovaný nick je přeškrtnutý)
, , ,  – ikona admina
, ,  – ikona karmy
– anonym

Po najetí na nick se zobrazí bublina s odkazem na profil. Zároveň je v ní pole na vaši soukromou poznámku. Ke každému nicku si můžete připojit vlastní poznámku, kterou vidíte jen vy.

Místnosti jsou dva základní typy, dočasné a stále. Dočasná je automaticky zrušena, pokud v ní nikdo nezůstane.

## Lomítkové příkazy

Každý uživatel může pro zrychlení použít příkazy, které umožní akci bez nutnosti klikání. Píšou se přímo do řádku pro psaní. Každý začíná lomítkem, které musí být hned na začátku řádku.

Pokud se příkaz použije na nick s mezerou, je potřeba jej napsat do uvozovek (např. /kick „otravný nick“ duvod).

Příkazy jsou:

    **/whisper**, /m, /w – šeptání. Např.: /whisper franci ahoj
    **/ignore**, /i – ignorovat. Např.: /i „otravný nick“

## Možnosti admina

### Zamykání

Přístup do místnosti lze omezit pro tři kategorie:

    **anonymy** [/noanon, /na]
    **mladší 18 let** [/lock18, /l18] – platí i pro anonymy a ty, kdo nemají v profilu vyplněný věk
    **všechny** [/lock, /l]

### Heslo
Správce může při zamknutí nastavit heslo, pomocí kterého lze vstoupit i do zamknuté místnosti. Funguje to tak, že místnost zamkne a **zároveň** nastaví i heslo (viz. obrázek). Při pokusu o vstup se uživateli zobrazí dotaz na heslo a pokud ho zadá správně, tak může vstoupit. Pokud už v místnosti byl, tak heslo znovu zadávat nemusí.
Pro **stálé místnosti** platí, že heslo vidí a může nastavit jen stálý správce a místnost je zamčená jen, pokud v ní aspoň jeden stálý správce je.

Místnost lze odemknout pomocí příkazu **/unlock** (/u).

### Smazání textu

Správce může smazat konkrétní řádek v chatu (pomocí ikony ) nebo všechny texty nějakého uživatele (pomocí ikony nebo příkazem **/smaz**). V druhém případě pak nemůže uživatel 1 minutu psát nové texty do místnosti.

### Posílání odkazů

Správce může nastavit, zda lze posílat odkazy do místnosti. Základní nastavení povoluje jen uživatelům s karmou. Lze buď povolit všem nebo naopak všem omezit. V případě omezení (i v případě, že uživatel nemá karmu) může správce na 5 minut povolit poslání odkazu pomocí příkazu **/link**.

### Vykopnutí

Správce může i vykopnout z místnosti pomocí příkazu **/kick**. U každého vykopnutí se musí uvést důvod. Zároveň jsou uložené všechny zprávy, které si správce a vykopnutý psali (i vzájemné šeptání). Room admini (, ) to mohou, v případě sporu, dohledat v administraci.
První vykopnutí je na 15 minut. Pokud byl člověk v posledních 24 hodinách vykopnutý z jakékoliv místnosti, je platnost prodloužena na 5 hodin.

### Změna admina

Admina lze předat pomocí příkazu **/admin**. Buď jej může aktuální správce dát někomu jinému nebo může správce s vyššími právy (stálý, room admin apod.) předat správce libovolně (někomu jinému nebo sám sobě).
