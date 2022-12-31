BEGIN;


CREATE TABLE IF NOT EXISTS public."Address"
(
    street character varying(20)[] COLLATE pg_catalog."default" NOT NULL,
    "number" character varying(10)[] COLLATE pg_catalog."default" NOT NULL,
    province character varying(25)[] COLLATE pg_catalog."default" NOT NULL,
    municipality character varying(20)[] COLLATE pg_catalog."default" NOT NULL,
    "ID" integer NOT NULL,
    CONSTRAINT "Address_pkey" PRIMARY KEY ("ID")
);

CREATE TABLE IF NOT EXISTS public."Person"
(
    "ID" integer NOT NULL,
    name character varying(15)[] COLLATE pg_catalog."default" NOT NULL,
    lastname character varying(15)[] COLLATE pg_catalog."default" NOT NULL,
    gender character varying(10)[] COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Person_pkey" PRIMARY KEY ("ID")
);

CREATE TABLE IF NOT EXISTS public."Placetolocation"
(
    "ID" integer NOT NULL,
    name character varying(20)[] COLLATE pg_catalog."default" NOT NULL,
    description character varying(100)[] COLLATE pg_catalog."default" NOT NULL,
    inuniversity boolean NOT NULL,
    CONSTRAINT "Placetolocation_pkey" PRIMARY KEY ("ID")
);

CREATE TABLE IF NOT EXISTS public."Students"
(
    "ID" integer NOT NULL,
    carrer character varying[] COLLATE pg_catalog."default" NOT NULL,
    yearofcarrer smallint NOT NULL,
    average real NOT NULL,
    degreeacttitude smallint NOT NULL,
    CONSTRAINT "Students_pkey" PRIMARY KEY ("ID")
);

CREATE TABLE IF NOT EXISTS public."Teachers"
(
    "ID" integer NOT NULL,
    departament character varying[] COLLATE pg_catalog."default" NOT NULL,
    leftcuba boolean NOT NULL,
    teachingcategory character varying[] COLLATE pg_catalog."default" NOT NULL,
    scientificcategory character varying[] COLLATE pg_catalog."default" NOT NULL,
    degreeacttitude smallint NOT NULL,
    CONSTRAINT "Teachers_pkey" PRIMARY KEY ("ID")
);


END;