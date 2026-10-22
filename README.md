[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/zeikar-kimcp-badge.png)](https://mseep.ai/app/zeikar-kimcp)

# KiMCP (Korea-integrated Model Context Protocol)

![](https://badge.mcpx.dev?type=server "MCP Server")
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<p align="center">
  <a href="README.en.md">🇺🇸 English</a> |
  <a href="README.md">🇰🇷 한국어</a>
</p>

KiMCP는 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)를 활용하여 [네이버](http://www.naver.com/), [카카오](https://www.kakaocorp.com/), [TMAP](https://www.tmapmobility.com/)과 같은 국내 API들을 LLM 애플리케이션에서 사용할 수 있는 MCP 서버입니다.

<p align="center">
  <img src="screenshots/screenshot-0.png" alt="스크린샷 1" style="width: 80%; height: auto; margin-bottom: 15px;">
  <img src="screenshots/screenshot-1.png" alt="스크린샷 2" style="width: 80%; height: auto;">
</p>

## Features

- **네이버 블로그 검색**: 네이버에서 블로그 콘텐츠 검색
- **네이버 뉴스 검색**: 네이버에서 뉴스 기사 검색
- **네이버 카페 검색**: 네이버 카페 커뮤니티에서 게시물 검색
- **네이버 지식iN 검색**: 네이버 지식iN에서 Q&A 게시물 검색
- **네이버 지역 검색**: 지역 업체 및 장소 정보 검색
- **네이버 이미지 검색**: 네이버에서 이미지 검색
- **다음 블로그 검색**: 다음 블로그에서 블로그 콘텐츠 검색
- **다음 카페 검색**: 다음 카페에서 게시물 검색
- **카카오맵 검색**: 카카오맵에서 장소 및 업체 정보 검색
- **자동차 길찾기**: 카카오맵을 사용하여 자동차 길찾기 정보 제공
- **대중교통 길찾기**: TMAP을 사용하여 대중교통 길찾기 정보 제공

현재 개발 중...

## Prerequisites

- [Claude Desktop](https://claude.ai/download)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python 패키지 관리자)
- 사용할 서비스의 API 키 (네이버, 카카오, SK Open API): [API 키 발급 가이드](docs/api-keys.md) 참고

## Installation

1. **저장소 복제**

   ```bash
   git clone https://github.com/zeikar/kimcp
   cd kimcp
   ```

2. **Python 의존성 설치**

   ```bash
   uv sync
   ```

3. **환경 변수 설정**

   프로젝트 루트에 제공된 `.env.example` 파일을 참고하여 `.env` 파일을 생성하세요:

   ```bash
   # .env.example 파일을 .env로 복사
   cp .env.example .env

   # 생성된 .env 파일 편집
   vi .env   # 또는 원하는 텍스트 에디터 사용
   ```

   `.env` 파일에 다음과 같이 API 키를 입력하세요:

   ```
   NAVER_CLIENT_ID=your_naver_client_id
   NAVER_CLIENT_SECRET=your_naver_client_secret
   KAKAO_REST_API_KEY=your_kakao_rest_api_key
   SK_APP_KEY=your_sk_app_key
   ```

   > **참고**:
   >
   > - 서비스별 키 발급 방법은 [API 키 발급 가이드](docs/api-keys.md)를 참고하세요.
   > - 필요한 API만 사용하는 경우, **해당 API 키만 설정**해도 됩니다.
   >   - API 키를 입력하지 않으면 **해당 MCP 도구가 자동으로 비활성화**됩니다. 예를 들어, 네이버 API 키만 입력하고 카카오 API 키를 입력하지 않으면 네이버 관련 도구만 사용 가능합니다.

4. **Claude Desktop에 설치**

   ```bash
   uv run mcp install main.py -f .env
   ```

5. **변경 사항을 적용하려면 Claude Desktop 재시작**

## Development

테스트 및 개발을 위한 MCP inspector 실행:

```bash
uv run mcp dev main.py
```

테스트 실행:

```bash
uv run pytest
```

기본 테스트는 실제 API를 호출하지 않습니다. 전체 도구를 실제 API로 호출하는 테스트는 `.env`의 키로 따로 실행하세요. 키가 없는 API의 도구는 건너뜁니다.

```bash
uv run --env-file .env pytest -m live
```

## Roadmap

- ✅ 네이버 API 통합
- ✅ 카카오 API 통합
- ✅ SK Open API 통합
- ⬜ 기상청(KMA) 통합
- 기타 등등

## License

이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## Acknowledgements

- [py-mcp-naver](https://github.com/pfldy2850/py-mcp-naver)
- [MCP](https://modelcontextprotocol.io/introduction)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [네이버 개발자 센터](https://developers.naver.com/main)
- [카카오 Developers](https://developers.kakao.com/)
- [TMAP](https://www.tmapmobility.com/)
- [Claude Desktop](https://claude.ai/download)
