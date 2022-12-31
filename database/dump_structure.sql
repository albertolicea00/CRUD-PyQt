--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

-- Started on 2022-12-31 18:38:37

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 24688)
-- Name: address; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.address (
    id integer NOT NULL,
    street character varying(20) NOT NULL,
    number character varying(10) NOT NULL,
    province character varying(25) NOT NULL,
    municipality character varying(20) NOT NULL
);


ALTER TABLE public.address OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 24687)
-- Name: address_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.address_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.address_id_seq OWNER TO postgres;

--
-- TOC entry 3350 (class 0 OID 0)
-- Dependencies: 209
-- Name: address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.address_id_seq OWNED BY public.address.id;


--
-- TOC entry 213 (class 1259 OID 24720)
-- Name: person; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.person (
    "ID" character varying(11) NOT NULL,
    name character varying(15) NOT NULL,
    lastname character varying(15) NOT NULL,
    gender character varying(10) NOT NULL,
    address integer NOT NULL,
    placetolocation integer NOT NULL,
    degreeacttitude smallint NOT NULL
);


ALTER TABLE public.person OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 24695)
-- Name: placetolocation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.placetolocation (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    description character varying NOT NULL,
    inuniversity boolean NOT NULL
);


ALTER TABLE public.placetolocation OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 24694)
-- Name: placetolocation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.placetolocation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.placetolocation_id_seq OWNER TO postgres;

--
-- TOC entry 3351 (class 0 OID 0)
-- Dependencies: 211
-- Name: placetolocation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.placetolocation_id_seq OWNED BY public.placetolocation.id;


--
-- TOC entry 215 (class 1259 OID 24768)
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    carrer character varying(20) NOT NULL,
    yearofcarrer smallint NOT NULL,
    average real NOT NULL
)
INHERITS (public.person);


ALTER TABLE public.student OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 24738)
-- Name: teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher (
    departament character varying(20) NOT NULL,
    leftcuba boolean NOT NULL,
    teachingcategory character varying(20) NOT NULL,
    scientificcategory character varying(20) NOT NULL
)
INHERITS (public.person);


ALTER TABLE public.teacher OWNER TO postgres;

--
-- TOC entry 3181 (class 2604 OID 24691)
-- Name: address id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address ALTER COLUMN id SET DEFAULT nextval('public.address_id_seq'::regclass);


--
-- TOC entry 3182 (class 2604 OID 24698)
-- Name: placetolocation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.placetolocation ALTER COLUMN id SET DEFAULT nextval('public.placetolocation_id_seq'::regclass);


--
-- TOC entry 3339 (class 0 OID 24688)
-- Dependencies: 210
-- Data for Name: address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.address (id, street, number, province, municipality) FROM stdin;
\.


--
-- TOC entry 3342 (class 0 OID 24720)
-- Dependencies: 213
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.person ("ID", name, lastname, gender, address, placetolocation, degreeacttitude) FROM stdin;
\.


--
-- TOC entry 3341 (class 0 OID 24695)
-- Dependencies: 212
-- Data for Name: placetolocation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.placetolocation (id, name, description, inuniversity) FROM stdin;
\.


--
-- TOC entry 3344 (class 0 OID 24768)
-- Dependencies: 215
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student ("ID", name, lastname, gender, address, placetolocation, degreeacttitude, carrer, yearofcarrer, average) FROM stdin;
\.


--
-- TOC entry 3343 (class 0 OID 24738)
-- Dependencies: 214
-- Data for Name: teacher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teacher ("ID", name, lastname, gender, address, placetolocation, degreeacttitude, departament, leftcuba, teachingcategory, scientificcategory) FROM stdin;
\.


--
-- TOC entry 3352 (class 0 OID 0)
-- Dependencies: 209
-- Name: address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.address_id_seq', 27, true);


--
-- TOC entry 3353 (class 0 OID 0)
-- Dependencies: 211
-- Name: placetolocation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.placetolocation_id_seq', 5, true);


--
-- TOC entry 3184 (class 2606 OID 24693)
-- Name: address address_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pkey PRIMARY KEY (id);


--
-- TOC entry 3190 (class 2606 OID 24724)
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY ("ID");


--
-- TOC entry 3186 (class 2606 OID 24702)
-- Name: placetolocation placetolocation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.placetolocation
    ADD CONSTRAINT placetolocation_pkey PRIMARY KEY (id);


--
-- TOC entry 3188 (class 2606 OID 24704)
-- Name: placetolocation placetolocation_unique; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.placetolocation
    ADD CONSTRAINT placetolocation_unique UNIQUE (name);


--
-- TOC entry 3194 (class 2606 OID 24772)
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY ("ID");


--
-- TOC entry 3192 (class 2606 OID 24767)
-- Name: teacher teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_pkey PRIMARY KEY ("ID");


--
-- TOC entry 3197 (class 2606 OID 24773)
-- Name: student addressRel; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT "addressRel" FOREIGN KEY (address) REFERENCES public.address(id) NOT VALID;


--
-- TOC entry 3195 (class 2606 OID 24783)
-- Name: teacher addressRel; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT "addressRel" FOREIGN KEY (address) REFERENCES public.address(id) NOT VALID;


--
-- TOC entry 3198 (class 2606 OID 24778)
-- Name: student placetolocationRel; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT "placetolocationRel" FOREIGN KEY (placetolocation) REFERENCES public.placetolocation(id) NOT VALID;


--
-- TOC entry 3196 (class 2606 OID 24788)
-- Name: teacher placetolocationRel; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT "placetolocationRel" FOREIGN KEY (placetolocation) REFERENCES public.placetolocation(id) NOT VALID;


-- Completed on 2022-12-31 18:38:37

--
-- PostgreSQL database dump complete
--

