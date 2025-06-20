-- Insert Users
INSERT INTO users (first_name, last_name, email, password, is_admin, id, created_at, updated_at) 
VALUES ("Admin", "Portfolio", "admin@portfolio.io", "$2b$12$JMgr7Zfi2w5KZwesW9mb8.UwneRbQvEF9gQqWA5VpVUifi8Ye8/fK", 1, "86d5a94f-ca6d-44b9-8910-3c5393386415", "2025-04-11 08:15:30.688366", "2025-04-11 08:15:30.688453"),
("Jane", "Doe", "jane@email.com", "$2b$12$et44er5sHplchE3IcnFySOu4VI/MNOxlld7yFyAlACz3pN8WoOthS", 0, "c867078b-eae0-4faf-8277-99771632baef", "2025-04-11 08:25:25.585981", "2025-04-11 08:25:25.586061"),
("Jennifer", "Smith", "jennifer@email.com", "$2b$12$9KuCsFkM6jz4hlXvAssLKODPqsogdCJ1vNvj9arthu5M9KRLl8Pse", 0, "24ae9b3c-5a63-4120-9aee-e84f503fc2d4", "2025-04-11 08:25:25.585981", "2025-04-11 08:25:25.586061"),
("John", "Doe", "john@email.com", "$2b$12$XI.VtuRyNnyLYhIkJM9QHet1CTrO3jMXfKfS5FNS.SyOpKXasF9C2", 0, "1c26cf6d-b05a-44e7-b694-c9d09b07f30d", "2025-04-11 08:25:25.585981", "2025-04-11 08:25:25.586061"),
("Mathieu", "Bernard", "mathieu@email.com", "$2b$12$xjhBibhGWEgnVMnDO3fTQ.U..df6DPi38FVg8hwSSidxiGYjMQ5tC", 0, "501618ff-4fc0-426f-a6f2-c9715ecf04bf", "2025-04-11 08:25:25.585981", "2025-04-11 08:25:25.586061"),
("Morgane", "Lardeux", "morgane@email.com", "$2b$12$utqR1BchnyeE6b/tJqHQfOMQkknDdzHDN9ojjv6XTu9aF7EHLELd2", 0, "4079e770-15ad-464e-9594-902b50e93ecf", "2025-04-11 08:25:25.585981", "2025-04-11 08:25:25.586061");

-- Insert Professions
INSERT INTO professions (title, description, price,  owner_id, id, created_at, updated_at)
VALUES ("Music", "2020-04-04 08:25:25.585981", "2020-04-04 08:25:25.585981"),
("Math", "Description", "2022-08-16 08:25:25.585981", "2022-08-16 08:25:25.585981"),
("History", "Description", "2025-02-21 08:25:25.585981", "2025-02-21 08:25:25.585981"),
("English", "Description", "2025-03-28 08:25:25.585981", "2025-03-28 08:25:25.585981"),
("Science", "Description", "2025-04-11 08:25:25.585981", "2025-04-11 08:25:25.585981");

-- Insert Reviews
INSERT INTO reviews (rating, text, place_id, user_id, id, created_at, updated_at)
VALUES (4, "I would recommend them to a friend, everything was made easy and understandable", "2021-07-22 08:25:25.585981", "2021-07-22 08:25:25.585981"),
(1, "Mediocre teaching, i learned nothing and had to do everything myself.", "2020-07-15 08:25:25.585981", "2020-07-15 08:25:25.585981"),
(3, "The sessions helped me but they lacked patience which deteriorated the experience.", "2024-08-18 08:25:25.585981", "2024-08-18 08:25:25.585981"),
(5, "Perfect teaching, they greatly helped my son with his schooling.", "2025-04-11 08:25:25.585981", "2025-04-11 08:25:25.585981"),
(4, "Useful for beginners, their teaching is clear and precise.", "2023-05-17 08:25:25.585981", "2023-05-17 08:25:25.585981"),
(3, "Good for short-term classes but the pedagogy is not the best.", "2021-06-10 08:25:25.585981", "2021-06-10 08:25:25.585981");
