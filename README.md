# BLOOM Revolt Bot

An AI text generation bot for Revolt, powered by BigScience's BLOOM.

## How to run

### System requirements

I'm not sure what the minimum system requirements are, but i've tested this on the following specs:

- OS: Ubuntu 22.04.2 LTS
- CPU: Intel Core i7-10700KF (8 cores, 16 threads)
- RAM: 32 GB DDR4 RAM
- GPU: NVIDIA GeForce RTX 3080

### Prerequisites

To run this you need to have the following installed:

- Node.js (16.x or newer)
- Python (3.8 or newer)

### Install dependencies

To install all dependencies, run:

```sh
yarn && pip install -r requirements.txt
```

### Running the bot

To run the bot, run:

```sh
yarn start:dev
```

and in another terminal, run:

```sh
cd model && python main.py
```

## License

The AI model is licensed under the BigScience Bloom RAIL 1.0 license, and the bot is licensed under the MIT license.
