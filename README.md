# Uluru Cultural Centre Multi-Agent System

A starter project exploring how a multi-agent visitor assistant could help
people respectfully learn about Aboriginal culture, ask questions in their
preferred language, and find their way around the visitor centre. The current
Python entry point illustrates the system architecture as a diagram; it is not
a functioning visitor assistant.

## Project overview

The conceptual flow starts with visitor input, identifies a language, and
routes the request to an Arrernte or Pitjantjatjara language specialist. A
knowledge-base lookup and cultural sensitivity checker support the response,
which is then reviewed by a translation verification agent before returning
to the visitor.

The checker and verifier in this starter are diagram components only. They do
not assess real content, provide translation, or replace guidance from
Aboriginal communities. Any future knowledge or language resources should be
used with the appropriate community permission and attribution.

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
