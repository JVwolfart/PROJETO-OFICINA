BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "usuarios" (
	"nome"	TEXT,
	"senha"	TEXT,
	"criar"	BOOLEAN,
	"editar"	BOOLEAN,
	"excluir"	BOOLEAN,
	"root"	BOOLEAN
);
INSERT INTO "usuarios" VALUES ('JOÃO VITOR','123456',1,1,1,1);
INSERT INTO "usuarios" VALUES ('JUNIOR','123456',1,1,1,1);
INSERT INTO "usuarios" VALUES ('MÁRCIA','123456',1,1,0,0);
INSERT INTO "usuarios" VALUES ('PAULO','123456',0,1,0,0);
INSERT INTO "usuarios" VALUES ('PEDRO','123456',0,0,0,0);
INSERT INTO "usuarios" VALUES ('CARLOS','123456',1,0,0,0);
COMMIT;
