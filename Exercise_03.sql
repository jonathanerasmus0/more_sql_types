-- Update 
UPDATE site_user
SET active_for = EXTRACT(EPOCH FROM CURRENT_TIMESTAMP - created_on) / (60 * 60 * 24);

-- Select name and active_for for all users
SELECT name, active_for
FROM site_user;