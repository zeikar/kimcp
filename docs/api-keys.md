# API 키 발급 가이드

KiMCP가 쓰는 서비스별 API 키를 발급하는 방법입니다. 발급한 키는 `.env`에 넣습니다. 필요한 서비스의 키만 넣어도 되고, 키가 없는 서비스의 도구는 자동으로 꺼집니다.

| 환경 변수 | 발급처 | 쓰는 도구 |
|---|---|---|
| `NAVER_CLIENT_ID`, `NAVER_CLIENT_SECRET` | [NAVER API HUB](#네이버-naver-api-hub) | 네이버 블로그, 뉴스, 카페, 지식iN, 지역, 이미지 검색 |
| `KAKAO_REST_API_KEY` | [Kakao Developers](#카카오-kakao-developers) | 다음 블로그, 카페 검색, 카카오맵 장소 검색, 자동차 길찾기 |
| `SK_APP_KEY` | [SK Open API](#sk-open-api-tmap-대중교통) | 대중교통 길찾기 |

## 네이버 (NAVER API HUB)

네이버 검색 API는 NAVER Cloud Platform의 NAVER API HUB에서 발급합니다. 네이버 개발자 센터는 2026년 7월 31일부터 검색 API 신규 신청을 받지 않고, 개발자 센터에서 발급한 키는 KiMCP에서 쓸 수 없습니다.

1. [NAVER Cloud Platform](https://www.ncloud.com)에 가입합니다. 개인도 가입할 수 있고, 결제 수단으로 신용카드를 꼭 등록해야 합니다.
2. 콘솔 오른쪽 위의 리전 & 플랫폼에서 Korea를 선택합니다.
3. Menu > All Services > Application Services > NAVER API HUB로 이동합니다.
4. Subscription에서 [서비스 이용 신청]을 누르고 약관에 동의합니다.
5. Application에서 [Application 등록]을 누르고 블로그, 뉴스, 카페, 지식iN, 지역, 이미지 검색 API를 선택합니다. 이름은 영문, 숫자, `-`만 써서 20자 이하로 짓습니다.
6. Application 목록의 [인증 정보]에 나오는 Client ID는 `NAVER_CLIENT_ID`에, Client Secret은 `NAVER_CLIENT_SECRET`에 넣습니다.

2026년 10월 기준으로 기간 한정 무료이고, 유료로 바뀌기 전에 공지됩니다. 검색 API는 키 하나당 하루 25,000회, 한 달 775,000회까지 호출할 수 있습니다. 자세한 내용은 [NAVER API HUB 이용 신청 가이드](https://guide.ncloud-docs.com/docs/apihub-application)를 참고하세요.

## 카카오 (Kakao Developers)

키 하나로 다음 검색, 카카오맵 장소 검색, 자동차 길찾기를 모두 쓸 수 있습니다.

1. [Kakao Developers](https://developers.kakao.com)에 로그인해 개발자로 등록하고, [앱 생성]으로 앱을 만듭니다. 앱 이름, 회사명, 카테고리는 필수이고, 개인 개발자는 회사명에 본인 이름을 넣어도 됩니다.
2. [앱] > [제품 설정] > [카카오맵]에서 사용 설정을 ON으로 바꿉니다. 꺼져 있으면 장소 검색이 `403 NotAuthorizedError`(`disabled OPEN_MAP_AND_LOCAL service`)로 실패합니다.
3. [앱] > [플랫폼 키] > [REST API 키]를 복사해 `KAKAO_REST_API_KEY`에 넣습니다. [호출 허용 IP 주소]는 비워 두세요. 값을 넣으면 그 밖의 IP에서는 `ip mismatched` 에러가 납니다.

2026년 10월 기준 무료 한도는 모든 API를 합쳐 한 달 300만 건이고, 장소 검색은 하루 10만 건, 자동차 길찾기는 하루 1만 건입니다. 카카오맵 무료 한도는 계정에서 카카오맵을 처음 켠 앱 하나에만 적용됩니다. 이미 카카오맵을 켠 앱이 있다면 새 앱 대신 그 앱의 키를 쓰세요. 자세한 한도는 [쿼터 문서](https://developers.kakao.com/docs/ko/getting-started/quota)에 있습니다.

6개월 동안 API 호출이나 설정 변경이 없으면 앱이 장기 미이용 상태가 되어 호출이 `SuspendedAppException` 에러로 막힙니다. 콘솔의 앱 목록에서 그 앱에 들어가 장기 미이용을 해제하면 다시 쓸 수 있습니다.

## SK Open API (TMAP 대중교통)

1. [SK Open API](https://openapi.sk.com/)에 가입하고 앱을 만들어 앱 키를 발급합니다.
2. 같은 앱에서 대중교통 API를 [사용 신청](https://openapi.sk.com/products/calc?svcSeq=59&menuSeq=393)합니다. 신청하지 않으면 키가 맞아도 `403 INVALID_API_KEY` 에러가 납니다.
3. 앱 키를 `SK_APP_KEY`에 넣습니다.

## 키 확인하기

키를 넣은 뒤 아래 명령으로 모든 도구를 실제 API로 호출해 볼 수 있습니다. 키가 없는 서비스의 도구는 건너뜁니다.

```bash
uv run --env-file .env pytest -m live
```
