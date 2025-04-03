# KiMCP (한국 특화 Model Context Protocol)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<p align="center">
  <a href="README.md">🇺🇸 English</a> |
  <a href="README.ko.md">🇰🇷 한국어</a>
</p>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)를 활용하여 네이버와 같은 한국 API들을 LLM 애플리케이션에 원활하게 통합하는 MCP 서버입니다.

![스크린샷](screenshots/screenshot-0.png)

## Features

- **네이버 블로그 검색**: 네이버에서 블로그 콘텐츠 검색
- **네이버 뉴스 검색**: 네이버에서 뉴스 기사 검색
- **네이버 카페 검색**: 네이버 카페 커뮤니티에서 게시물 검색
- **네이버 지식iN 검색**: 네이버 지식iN에서 Q&A 게시물 검색
- **네이버 지역 검색**: 지역 업체 및 장소 정보 검색
- **네이버 이미지 검색**: 네이버에서 이미지 검색
- **네이버 쇼핑 검색**: 네이버 쇼핑에서 상품 검색 및 가격 비교
- 현재 개발 중...

## Prerequisites

- [Claude Desktop](https://claude.ai/download)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python 패키지 관리자)
- [네이버 API Key](https://developers.naver.com/apps/#/register)

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

   ```bash
   echo "NAVER_CLIENT_ID=your_naver_client_id" > .env
   echo "NAVER_CLIENT_SECRET=your_naver_client_secret" >> .env

   # 선택 사항: 기본 uv Python 버전이 너무 오래된 경우 설정
   echo "UV_PYTHON=3.10" >> .env
   ```

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

## Roadmap

- ✅ 네이버 API 통합
- ⬜ 카카오 API 통합
- ⬜ 기상청(KMA) 통합
- 기타 등등

## License

이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## Acknowledgements

- [py-mcp-naver](https://github.com/pfldy2850/py-mcp-naver)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [네이버 개발자 센터](https://developers.naver.com/main)
