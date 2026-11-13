# CI/CD DevOps -harjoitus

[![Python CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)

Pieni Python-sovellus, jolle GitHub Actions ajaa linttauksen, testit ja tekee zip-artifactin jokaisesta pushista ja pull requestista.

## Ajo-ohjeet

```bash
pip install -r requirements.txt
ruff check .
pytest -q
python app.py
```

## Workflow-ajot

- Onnistunut ajo: <LINKKI>
- Epäonnistunut ajo: <LINKKI TAI KUVAKAAPPAUS>

## Virhe ja korjaus

Muutin testin odotukseksi `add(2, 3) == 6`. Ajo kaatui stepissä **Run unit tests**, ja lokissa näkyi `AssertionError: assert 5 == 6`. Korjasin odotuksen takaisin arvoon `== 5`, minkä jälkeen ajo meni läpi.

## Turvallisuus ja kustannukset

- Workflow:lla on vain lukuoikeus (`permissions: contents: read`).
- Repossa ei ole salasanoja tai avaimia. Pilvideploymentissa käyttäisin OIDC:tä pitkäikäisten avainten sijaan.
- `timeout-minutes: 10` ja artifactin 7 päivän säilytys pitävät käytön ja kustannukset pieninä.
