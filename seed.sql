

TRUNCATE TABLE FILMS;
TRUNCATE TABLE DIRECTORS;

ALTER SEQUENCE films_id_seq RESTART WITH 1;
ALTER SEQUENCE directors_id_seq RESTART WITH 1;

INSERT INTO directors(director_id, name, birth) VALUES (1, 'Gyula Gazdag', 1947);
INSERT INTO directors(director_id, name, birth) VALUES (2, 'Béla Tarr', 1955);
INSERT INTO directors(director_id, name, birth) VALUES (3, 'Miklós Jancsó', 1921);

-- Gyula Gazdag films
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Long Distance Runner','Hosszú futásodra mindig számíthatunk...', 1969, False, 1, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Selection', 'A válogatás', 1970, True, 1, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Whistling Cobblestone', 'A sípoló macskakő', 1971, True, 1, True, False);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Resolution', 'A határozat', 1972, True, 1, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Singing on the Treadmill', 'Bástyasétány hetvennégy', 1974, True, 1, True, False);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Swap', 'A kétfenekű dob', 1978, True, 1, True, False);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Banquet', 'A bankett', 1982, False, 1, True, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Lost Illusions', 'Elveszett illúziók', 1983, False, 1, True, False);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Package Tour', 'Társasutazás', 1985, False, 1, True, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('A Hungarian Fairy Tale', 'Hol volt, hol nem volt...', 1987, False, 1, True, False);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Stand Off', 'Túsztörténet', 1989, False, 1, True, False);

-- Bela Tarr films
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Family Nest', 'Családi tűzfészek', 1977, False, 2, False, False);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Outsider', 'Szabadgyalog', 1978, True, 2, True, False);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Prefab People','Panelkapcsolat ', 1982, False, 2, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Almanac of Fall','Őszi almanach', 1985, False, 2, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Damnation','Kárhozat', 1988, False, 2, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Santans Tango','Sátántangó ', 1994, False, 2, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('Wreckmeister Harmonies','Werckmeister harmóniák ', 2000, False, 2, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Man From London','A londoni férfi', 2007, False, 2, False, True);
INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ('The Turin Horse','A torinói ló ', 2011, False, 2, False, True);

-- Miklós Jancsó films
-- INSERT INTO films(title_en, title_hu, year, was_banned, directed_by, restored, is_documentary) VALUES ()


