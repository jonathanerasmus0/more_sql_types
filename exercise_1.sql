-- Create the site_user table 
CREATE TABLE IF NOT EXISTS site_user (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  uuid UUID UNIQUE NOT NULL,
  avatar BYTEA,
  role VARCHAR(20) CHECK (role IN ('Anonymous', 'Guest', 'User', 'Moderator', 'Admin')),
  birthdate DATE,
  siblings TEXT[],
  availability TIME WITHOUT TIME ZONE[],
  site_settings JSONB,
  created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  active_for INTEGER NOT NULL DEFAULT 0
);

-- Inserting the DATA INTO THE site_user table
INSERT INTO site_user (
  name, uuid, role, birthdate, siblings, availability, site_settings, created_on
) VALUES
  -- Miriam Valira
  ('Miriam Valira', 
   'e41e1291-33b8-4316-8a86-28a618d5c338', 
   'Admin', 
   '1995-08-29', 
   '{"Dani","Louis"}', 
   '{{12:00:00,15:00:00}}', 
   '{"background": "red", "notifications": false}',
   CURRENT_TIMESTAMP
  ),
  -- Johann Müller
  ('Johann Müller', 
   'd81331bf-a4f6-4ecd-8883-51dee509309e', 
   'User', 
   '2002-05-09', 
   '{}', 
   '{{09:00:00,14:00:00},{18:00:00,20:00:00}}', 
   '{"notifications": true}',
   CURRENT_TIMESTAMP
  ),
  -- Louise Clark
  ('Louise Clark', 
   'e6168ec9-7306-44a5-9875-2c659e15740e', 
   'Moderator', 
   '1992-05-03', 
   '{"Monique"}', 
   '{{09:00:00,12:00:00},{13:00:00,17:00:00}}', 
   '{"notifications": true}',
   CURRENT_TIMESTAMP
  );

-- Select all users from the site_user table
SELECT *
FROM site_user;
