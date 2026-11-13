# CI/CD DevOps -harjoitus

[![Python CI](https://github.com/oskarimarkula/CI-CD_devops/actions/workflows/ci.yml/badge.svg)](https://github.com/oskarimarkula/CI-CD_devops/actions/workflows/ci.yml)

Pieni Python-sovellus, jolle GitHub Actions ajaa linttauksen, testit ja tekee zip-artifactin jokaisesta pushista ja pull requestista.

## Ajo-ohjeet

```bash
pip install -r requirements.txt
ruff check .
pytest -q
python app.py
```

## Workflow-ajot

- Onnistunut ajo: https://github.com/OskariMarkula/CI-CD_devops/actions/runs/43415022885
- Epäonnistunut ajo: https://github.com/OskariMarkula/CI-CD_devops/actions/runs/43415249288 ([virherivi lokissa](https://github.com/OskariMarkula/CI-CD_devops/actions/runs/43415249288/job/131851386824#step:6:26))

## Virhe ja korjaus

Muutin testin odotukseksi `add(2, 3) == 6` (commit "testi 1"). Ajo kaatui stepissä **Run unit tests**, ja lokissa näkyi:

```
>       assert add(2, 3) == 6
E       assert 5 == 6
E        +  where 5 = add(2, 3)

test_app.py:7: AssertionError
FAILED test_app.py::test_add - assert 5 == 6
```

Lokista näkee, että funktio palautti oikean arvon 5, mutta testi odotti arvoa 6, eli virhe oli testissä eikä sovelluksessa. Korjasin odotuksen takaisin arvoon `== 5`, minkä jälkeen ajo meni taas läpi.

## Turvallisuus ja kustannukset

- Workflow:lla on vain lukuoikeus (`permissions: contents: read`).
- Repossa ei ole salasanoja tai avaimia. Pilvideploymentissa käyttäisin OIDC:tä pitkäikäisten avainten sijaan.
- `timeout-minutes: 10` ja artifactin 7 päivän säilytys pitävät käytön ja kustannukset pieninä.
