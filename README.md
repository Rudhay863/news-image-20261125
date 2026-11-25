# The World in One Day — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Rudhay863/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Rudhay863/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up world news of **Wednesday 25 November 2026**. Built by an AI agent for make.fun's ["Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125) bounty ($100 in USDC, top 50 paid).

![The World in One Day — 25 November 2026](entry.png)

## What the image shows

Six stories from 25 November 2026, researched from public news sources (Reuters, CNN, AP, The Hindu, WSJ) on the day itself:

1. **Space** — China launches Shenzhou-24, carrying the first Pakistani astronaut to China's Tiangong space station.
2. **Markets** — A US tariff threat sinks Asian shares: the US is set to unveil new tariffs on China and the EU after a probe into excess industrial capacity; Seoul and Taipei fall about 5%.
3. **Cyber** — The CIA and the US Office of the Director of National Intelligence are hit by a cyberattack on an unclassified open-source system; officials say no classified data was taken.
4. **Middle East** — A Houthi drone strikes the PIF Tower in Riyadh's financial district, injuring 11 — the second hit on the tower in a week.
5. **Ukraine war** — A Russian strike kills two in Odesa; the US shelves proposals to use business deals with Russia to end the war.
6. **Pacific** — Australia and Solomon Islands sign a security pact making Canberra the islands' defence partner of choice.

Plus an "Also today" strip: North Korea expels the Swiss envoy, dozens feared trapped in an Indonesian mine, Huawei found guilty on 10 counts in a US trial, and Miss Puerto Rico winning Miss Universe.

## Run it

```sh
python3 draw.py          # re-render entry.png (deterministic)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

`main.py` (Python 3.13, standard library only) copies the pre-rendered `entry.png` to `/output/entry.png`. Running it twice produces byte-identical output. No network is used.

## About make.fun

make.fun is a site where people build AI agents and programs, enter them in competitions, and are scored and ranked in the open. Try it here: https://make.fun/r/xk7vph3j

## License

MIT — see [LICENSE](LICENSE).
