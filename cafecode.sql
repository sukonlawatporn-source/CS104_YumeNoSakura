CREATE TABLE customers (
    cus_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone INTEGER,
    email TEXT
);

CREATE TABLE games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name TEXT NOT NULL,
    type TEXT,
    size_gb REAL
);

CREATE TABLE computers (
    com_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pc_name TEXT NOT NULL,
    game_id INTEGER,
    status TEXT,
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);

CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cus_id INTEGER,
    com_id INTEGER,
    start_time Text,
    hours TEXT,
    FOREIGN KEY (cus_id) REFERENCES customers(cus_id),
    FOREIGN KEY (com_id) REFERENCES computers(com_id)
);

CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER,
    price REAL,
    method TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

INSERT INTO customers (name, phone, email) VALUES
('John Doe', '0811111111', 'john@gmail.com'),
('Alice Smith', '0822222222', 'alice@gmail.com'),
('Michael Lee', '0833333333', 'michael@gmail.com'),
('Emma Brown', '0844444444', 'emma@gmail.com'),
('David Wilson', '0855555555', 'david@gmail.com'),
('Sophia Taylor', '0866666666', 'sophia@gmail.com'),
('Daniel Kim', '0877777777', 'daniel@gmail.com'),
('Olivia White', '0888888888', 'olivia@gmail.com'),
('James Anderson', '0899999999', 'james@gmail.com'),
('Liam Scott', '0800000000', 'liam@gmail.com');

INSERT INTO games (game_name, type, size_gb) VALUES
('Valorant', 'FPS', 30),
('Minecraft', 'Sandbox', 5),
('League of Legends', 'MOBA', 20),
('Dota 2', 'MOBA', 40),
('PUBG', 'Battle Royale', 50),
('Fortnite', 'Battle Royale', 45),
('GTA V', 'Open World', 100),
('Apex Legends', 'FPS', 70),
('Counter Strike 2', 'FPS', 35),
('Roblox', 'Sandbox', 3);

INSERT INTO computers (pc_name, game_id, status) VALUES
('PC-01', 1, 'Available'),
('PC-02', 2, 'Occupied'),
('PC-03', 3, 'Available'),
('PC-04', 4, 'Maintenance'),
('PC-05', 5, 'Available'),
('PC-06', 6, 'Occupied'),
('PC-07', 7, 'Available'),
('PC-08', 8, 'Available'),
('PC-09', 9, 'Occupied'),
('PC-10', 10, 'Available');

INSERT INTO bookings (cus_id, com_id, start_time, hours) VALUES
(1, 1, '2026-05-10 10:00:00', 2),
(2, 2, '2026-05-10 11:00:00', 3),
(3, 3, '2026-05-10 12:00:00', 1),
(4, 4, '2026-05-10 13:00:00', 4),
(5, 5, '2026-05-10 14:00:00', 2),
(6, 6, '2026-05-10 15:00:00', 5),
(7, 7, '2026-05-10 16:00:00', 1),
(8, 8, '2026-05-10 17:00:00', 3),
(9, 9, '2026-05-10 18:00:00', 2),
(10, 10, '2026-05-10 19:00:00', 4);

INSERT INTO payments (booking_id, price, method) VALUES
(1, 50, 'Cash'),
(2, 75, 'Credit Card'),
(3, 30, 'Cash'),
(4, 120, 'QR PromptPay'),
(5, 70, 'Cash'),
(6, 175, 'Credit Card'),
(7, 40, 'Cash'),
(8, 120, 'QR PromptPay'),
(9, 90, 'Cash'),
(10, 80, 'Credit Card');