# API Key Guide

How to get the API key for each service KiMCP uses. Put the keys in `.env`. You only need keys for the services you want; tools for a service without a key are disabled automatically.

The consoles below are in Korean, so menu and button names are given as they appear, with an English gloss.

| Environment variable | Issued by | Tools |
|---|---|---|
| `NAVER_CLIENT_ID`, `NAVER_CLIENT_SECRET` | [NAVER API HUB](#naver-naver-api-hub) | Naver blog, news, cafe, Knowledge iN, local, and image search |
| `KAKAO_REST_API_KEY` | [Kakao Developers](#kakao-kakao-developers) | Daum blog and cafe search, Kakao Map place search, car directions |
| `SK_APP_KEY` | [SK Open API](#sk-open-api-tmap-transit) | Transit directions |

## Naver (NAVER API HUB)

Naver search API keys come from NAVER API HUB on NAVER Cloud Platform. The Naver Developer Center stopped taking new search API applications on 2026-07-31, and keys issued there don't work with KiMCP.

1. Sign up for [NAVER Cloud Platform](https://www.ncloud.com). Individuals can sign up, but registering a credit card as the payment method is required.
2. In the console, choose Korea under Region & Platform at the top right.
3. Go to Menu > All Services > Application Services > NAVER API HUB.
4. In Subscription, click [서비스 이용 신청] (apply for the service) and accept the terms.
5. In Application, click [Application 등록] (register application) and select the blog, news, cafe, Knowledge iN, local, and image search APIs. The name can be up to 20 characters of letters, digits, and `-`.
6. Open [인증 정보] (credentials) for the application in the Application list. Put the Client ID in `NAVER_CLIENT_ID` and the Client Secret in `NAVER_CLIENT_SECRET`.

As of October 2026 it's free for a limited time, and the switch to paid plans will be announced beforehand. Search APIs allow 25,000 calls a day and 775,000 a month per key. See the [NAVER API HUB application guide](https://guide.ncloud-docs.com/docs/apihub-application) for details.

## Kakao (Kakao Developers)

One key covers Daum search, Kakao Map place search, and car directions.

1. Log in to [Kakao Developers](https://developers.kakao.com), register as a developer, and create an app with [앱 생성] (create app). App name, company name, and category are required; individual developers can enter their own name as the company name.
2. Turn on [앱] > [제품 설정] > [카카오맵] (App > Product settings > Kakao Map). If it's off, place search fails with `403 NotAuthorizedError` (`disabled OPEN_MAP_AND_LOCAL service`).
3. Copy the key from [앱] > [플랫폼 키] > [REST API 키] (App > Platform keys > REST API key) into `KAKAO_REST_API_KEY`. Leave [호출 허용 IP 주소] (allowed IP addresses) empty; if you set it, calls from any other IP fail with `ip mismatched`.

As of October 2026 the free quota is 3,000,000 calls a month across all APIs, with 100,000 a day for place search and 10,000 a day for car directions. The free Kakao Map quota applies only to the first app in your account that turned on Kakao Map, so if you already have one, use that app's key instead of a new app. See the [quota docs](https://developers.kakao.com/docs/ko/getting-started/quota) for details.

An app with no API calls or settings changes for 6 months becomes inactive, and calls fail with `SuspendedAppException`. Open the app from the app list in the console and lift the inactive status to use it again.

## SK Open API (TMAP Transit)

1. Sign up for [SK Open API](https://openapi.sk.com/), create an app, and get its app key.
2. In the same app, [apply for the Transit API](https://openapi.sk.com/products/calc?svcSeq=59&menuSeq=393). Without this, calls fail with `403 INVALID_API_KEY` even with a valid key.
3. Put the app key in `SK_APP_KEY`.

## Checking your keys

After adding your keys, this calls every tool against the real APIs. Tools for a service without a key are skipped.

```bash
uv run --env-file .env pytest -m live
```
