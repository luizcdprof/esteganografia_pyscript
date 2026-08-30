# 👁️‍🗨️ Esteganografia LSB — Cyber Blue | Projeto Feira de Tecnologia

Aplicação web interativa para ocultar e revelar mensagens secretas em imagens (PNG) utilizando a técnica de **Esteganografia em LSB (*Least Significant Bit*)**. 

O projeto roda **100% no navegador** via PyScript/WebAssembly, sem dependência de servidores backend, e conta com uma suíte de **testes unitários automatizados com Pytest**.

---

## 🚀 Tecnologias Utilizadas

* **Python 3** — Manipulação de dados binários, bitwise operators e lógica LSB.
* **PyScript & Pyodide** — Execução do código Python no navegador com suporte à API do HTML5 Canvas.
* **HTML5 & CSS3** — Interface estilizada com paleta *Cyber Blue* e animações de neon.
* **Google Fonts & Material Symbols** — Tipografia estilizada (*Share Tech Mono* / *Rajdhani*) e ícone de interface.
* **Pytest** — Framework de testes automatizados para validação da lógica de ocultação e conversão de bits.

---

## 🛠️ Estrutura do Projeto

```text
├── index.html              # Interface HTML5 com suporte a Upload/Download e PyScript
├── style.css               # Estilização visual (Cyber Blue & Google Fonts)
├── esteganografia.py       # Lógica pura em Python (conversão de bits e algoritmo LSB)
├── main.py                 # Manipulação do DOM e integração do Canvas via PyScript
└── test_esteganografia.py  # Testes unitários automatizados com Pytest