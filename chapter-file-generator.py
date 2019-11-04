import os

data = [
	[['opis', 'Opis i cel projektu'], [['inspiracja', 'Inspiracja'], ['opis', 'Opis projektu'], ['cele', 'Główne cele projektu'], ['uzytkownicy', 'Interesariusze i użytkownicy']]],
	[['wymagania', 'Specyfikacja wymagań projektu'], [['funkcjonalne', 'Wymagania funkcjonalne'], ['jakosciowe', 'Wymagania jakościowe'], ['techniczne', 'Wymagania techniczne'], ['przypadki_uzycia', 'Przypadki użycia']]],
	[['dane', 'Przygotowywanie danych wejściowych'], [['zrodlo', 'Źródło danych'], ['pobieranie', 'Pobieranie i dekompresja'], ['parsowanie', 'Parsowanie informacji'], ['struktura', 'Tworzenie struktury grafu'], ['narzedzie', 'Narzędzie WikiGraph Parser']]],
	[['implementacja', 'Implementacja głównej aplikacji WikiGraph'], [['model', 'Model danych'], ['reprez_wizualna', 'Wizualna reprezentacja węzłów i połączeń'], ['tryby_widoki', 'Tryby poruszania się i widoki węzła'], ['historia_trasy', 'Historia przeglądania oraz zaprogramowane trasy'], ['integracja_cave', 'Integracja z jaskinią'], ['konsola', 'Konsola operatora'], ['Linia_czasu', 'Linia czasu']]],
	[['konfiguracja', 'Konfiguracja i uruchamianie'], []],
	[['eksperyment', 'Eksperyment'], []],
	[['podsumowanie', 'Podsumowanie'], []]
]
output = '../rozdzialy'


def mkdir(name):
	if not os.path.exists(name):
		os.makedirs(name)


mkdir(output)
os.chdir(output)
index = 1
for chapter in data:
	name = str(index) + '_' + chapter[0][0]
	mkdir(name + '/img')
	os.chdir(name)
	open('img/.gitignore', 'w').close()
	print('\\input{rozdzialy/' + name + '/rozdzial.tex}')

	sub_index = 1
	with open('rozdzial.tex', 'w') as chapter_file:
		chapter_file.write('\\chapter{' + chapter[0][1] + '}\n\n')

		for sub_chapter in chapter[1]:
			sub_name = str(sub_index) + '_' + sub_chapter[0]
			chapter_file.write('\\input{rozdzialy/' + name + '/' + sub_name + '.tex}\n')
			with open(sub_name + '.tex', 'w') as sub_chapter_file:
				sub_chapter_file.write('\\section{' + sub_chapter[1] + '}\n')
				sub_chapter_file.close()
			sub_index += 1
		chapter_file.close()
	index += 1
	os.chdir('../')
