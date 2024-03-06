-- Exercise 1 for PART 2 

SELECT name
FROM site_user
WHERE array_length(siblings, 1) > 1;

UPDATE site_user
SET siblings = array_append(siblings, 'Jordi')
WHERE name = 'Louise Clark';

UPDATE site_user
SET availability = ARRAY[[time '09:00:00', time '10:00:00']]
WHERE name = 'Louise Clark';

UPDATE site_user
SET site_settings = jsonb_set(site_settings, '{notifications}', 'false')
WHERE name = 'Louise Clark';

SELECT name, role
FROM site_user
WHERE role < 'Moderator';

SELECT name
FROM site_user
WHERE site_settings @> '{ "notifications": false }';

SELECT name
FROM site_user
WHERE site_settings IS NULL OR NOT (site_settings @> '{ "background": '*' }');

