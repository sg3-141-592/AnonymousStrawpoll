ALTER TABLE polls
ADD COLUMN pollType text;

UPDATE polls SET pollType = "SENTIMENT";