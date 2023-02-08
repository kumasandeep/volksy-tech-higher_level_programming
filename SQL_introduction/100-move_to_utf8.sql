-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table
ALTER DATABASE hbtn_0c_0 CHARACTER SET COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHARACTER SET COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY `name` VARCHAR(256) CHARACTER SET COLLATE utf8mb4_unicode_ci;
