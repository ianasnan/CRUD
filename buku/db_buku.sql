--
-- PostgreSQL database dump
--

-- Dumped from database version 10.19
-- Dumped by pg_dump version 10.1

-- Started on 2023-05-27 15:03:11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12924)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2799 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 196 (class 1259 OID 168148)
-- Name: data_buku; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE data_buku (
    id_buku text NOT NULL,
    judulbuku text,
    deskripsi text,
    kategori text,
    keyword text,
    harga numeric(17,2),
    penerbit text
);


ALTER TABLE data_buku OWNER TO postgres;

--
-- TOC entry 2792 (class 0 OID 168148)
-- Dependencies: 196
-- Data for Name: data_buku; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY data_buku (id_buku, judulbuku, deskripsi, kategori, keyword, harga, penerbit) FROM stdin;
asd	ian	asd	asd	asd	123.00	asd
\.


--
-- TOC entry 2670 (class 2606 OID 168157)
-- Name: data_buku data_buku_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY data_buku
    ADD CONSTRAINT data_buku_pkey PRIMARY KEY (id_buku);


-- Completed on 2023-05-27 15:03:11

--
-- PostgreSQL database dump complete
--

