Page Object Model (POM) to popularny wzorzec projektowy stosowany w testach automatycznych. 
Zakłada on, że dla każdej strony aplikacji tworzymy osobną klasę, która reprezentuje tę stronę 
oraz jej elementy (przyciski, pola tekstowe itp.). Dzięki temu możemy łatwiej utrzymywać kod testów 
i ponownie wykorzystywać metody przypisane do poszczególnych stron.

Dlaczego używać POM?
Separacja logiki strony od logiki testowej: Kod związany z operacjami na stronie znajduje się w klasie strony, a scenariusze testowe tylko wywołują odpowiednie metody.
Lepsza czytelność i utrzymywalność: Zmiany w interfejsie użytkownika wymagają modyfikacji jedynie w klasie strony, a nie we wszystkich testach.
Reużywalność: Te same metody strony mogą być wykorzystywane w różnych testach.