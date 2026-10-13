<img width="1536" height="1024" alt="interactive guide agent " src="https://github.com/user-attachments/assets/6bc40514-0d13-4b3c-911e-9a0830180faf" />
# Uluru Cultural Centre Multi-Agent System

A starter project exploring how a multi-agent visitor assistant could help
people respectfully learn about Aboriginal culture, ask questions in their
preferred language, and find their way around the visitor centre. The current
Python entry point illustrates the system architecture as a diagram; it is not
a functioning visitor assistant.

## Project goal

This repository demonstrates the intended shape of a culturally respectful,
multi-agent visitor experience for the Uluru Cultural Centre. It is designed
as a conceptual prototype to show how language routing, knowledge lookup,
and response review could work together in a future assistant.

## Ethics and cultural guidance

This project is only a starter and must not be treated as an authoritative
source on Aboriginal culture, language, or visitor guidance. Any future use of
community knowledge, translations, or cultural content should be developed in
consultation with the relevant Aboriginal communities, with permission,
accurate attribution, and careful review.

The checker and verifier in this starter are diagram components only. They do
not assess real content, provide translation, or replace guidance from
Aboriginal communities.

## Project overview

The conceptual flow starts with visitor input, identifies a language, and
routes the request to an Arrernte or Pitjantjatjara language specialist. A
knowledge-base lookup and cultural sensitivity checker support the response,
which is then reviewed by a translation verification agent before returning
to the visitor.

Any future knowledge or language resources should be used with the appropriate
community permission and attribution.

## Features

- A clear, editable diagram of the proposed multi-agent flow.
- Visual distinctions for visitor, agent, and tool nodes.
- Explicit positions and optional labels to make the architecture easy to
  extend.
- A generated PNG diagram for sharing or discussion.

## Architecture diagram

The diagram is generated in the repository root when you run the script:

![Conceptual multi-agent system architecture](Uluru_Cultural_Center_Extended_System.png)

## Run locally

Requires Python 3. Install the diagram dependencies and run the entry point:

```bash
python -m pip install matplotlib networkx
python extended_uluru.py
```

The script saves `Uluru_Cultural_Center_Extended_System.png` in the current
working directory.
