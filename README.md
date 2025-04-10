# NCloud Cloud Insight Exporter

Naver Cloud의 Cloud Insight API를 활용하여 서버, 로드밸런서, Redis, NAS 등의 모니터링 지표를 Prometheus 포맷으로 수집 및 제공하는 Exporter입니다.

## 주요 기능

- NCloud API를 호출하여 다양한 리소스의 Metric 수집
- Prometheus에서 수집할 수 있도록 `/metrics` Endpoint 제공
- 비동기 방식(metric 병렬 수집)을 통한 성능 향상
- 설정 파일 기반의 유연한 리소스 정의

## 실행 방법

### 로컬 실행

```bash
python main.py
```

### Docker 실행

```bash
docker build -t ncloud-exporter .
docker run -p 9000:9000 ncloud-exporter
```

## HTTP Endpoint

- `/` : 기본 페이지
- `/health` : 헬스 체크
- `/metrics` : Prometheus에서 scrape할 수 있는 metrics 제공 (비동기)

## 설정 (config.yaml)

- `log_level`: 로그 출력 레벨 (`INFO`, `DEBUG`)
- `api_urls`: NCloud API 엔드포인트
- `resource_types`: 모니터링 대상 리소스 정의
  - 리소스별 API 호출 메서드, 메트릭 키, 식별 키 등 포함
- `environments`: 환경별 설정 덮어쓰기 가능 (`DEV`, `PRD`)

## 구조

- `main.py` : Flask 기반 웹 서버 및 Metric Exporter 호출
- `common.py` : 공통 유틸리티 (로깅, 시간 처리 등)
- `config.yaml` : 환경별 설정 파일
- `exporter/metric_exporter.py` : Metric 수집 로직 구현부 (별도 정의 필요)

## 요구사항

- Python 3.8+
- Flask
- Prometheus Client
- asyncio

## Prometheus 설정 예시

Prometheus가 본 Exporter를 scrape 하도록 설정하려면 `prometheus.yml`에 아래와 같이 job을 추가합니다:

```yaml
scrape_configs:
  - job_name: 'ncloud-exporter'
    static_configs:
      - targets: ['<exporter_host>:9000']
```

> `exporter_host`는 해당 Exporter가 실행되고 있는 호스트의 IP 또는 도메인입니다.

## Grafana 연동

Grafana에서는 Prometheus 데이터를 기반으로 다양한 시각화를 구성할 수 있습니다. 주요 지표는 다음과 같습니다:

- 서버: `avg_cpu_used_rto`, `mem_usert`, `avg_rcv_bps` 등
- Redis: `redis_connected_clients`, `mem_pct`, `cpu_sys` 등
- NAS: `volume_used_ratio`, `volume_size` 등
- 로드밸런서: `concurrent_session`, `traffic_in_byte` 등

### 대시보드 템플릿 제안

다음과 같은 구성으로 대시보드를 만들 수 있습니다:

- **리소스별 CPU/Memory/Traffic 트렌드 그래프**
- **Top N CPU 사용률 높은 서버**
- **Redis 메모리 사용량 모니터링**
- **NAS 저장소 사용률 경고 임계값 시각화**

> 대시보드는 템플릿 JSON 파일로 추후 공유 가능합니다. 사내 운영환경에 맞춰 사용자 정의 가능합니다.

