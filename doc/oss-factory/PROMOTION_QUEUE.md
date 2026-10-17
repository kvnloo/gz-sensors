# Gazebo Sensors — fork-local promotion queue

> Coordination-only on `kvnloo/gz-sensors:coordination/promotion-queue`; not merged into any default branch. This is the **single current downstream project queue**, superseding the **location** of legacy factory #147, not the historical source record. No origin write, worker lease, CI approval or upstream merge is authorized.

**Origin:** https://github.com/gazebosim/gz-sensors  
**Downstream:** https://github.com/kvnloo/gz-sensors  
**Historical source (read-only archive):** https://github.com/kvnloo/oss-factory/issues/147  
**Factory directory (links only):** https://github.com/kvnloo/oss-factory/issues/14

## Current merge gates — 2026-10-17

| Carrier | Exact head | Disposition / next executable action |
|---|---|---|
| [Origin sensors #664](https://github.com/gazebosim/gz-sensors/pull/664) | `fff5fab51561a96ff63785a4a49b5dc6d6fcc19b` | **ORIGIN_LIVE / owner direction pending.** Maintainer iche033 diagnosed Ogre2 projection as root cause; let their rendering [#1390](https://github.com/gazebosim/gz-rendering/pull/1390) land before any competing sensor fix. Native Ogre2 NOT_RUN in this coordination migration. |
| [Rendering #1390](https://github.com/gazebosim/gz-rendering/pull/1390) | `0fad5d7b0bc4dcaed6fd2e3166aa85d0b221ef54` | **EXTERNAL OWNER / WATCH_ONLY.** Renderer not registered as a separate factory project. Do not claim implementation or post redundant origin work. |
| [Fork #1](https://github.com/kvnloo/gz-sensors/pull/1) / [origin #663](https://github.com/gazebosim/gz-sensors/pull/663) | See historical record | **LANDED / SUPERSEDED**; do not repeat. |
| [Fork #2](https://github.com/kvnloo/gz-sensors/pull/2), [#6](https://github.com/kvnloo/gz-sensors/pull/6), [#3](https://github.com/kvnloo/gz-sensors/pull/3), [#4](https://github.com/kvnloo/gz-sensors/pull/4), [#5](https://github.com/kvnloo/gz-sensors/pull/5), [LiDAR c0b3d1ca](https://github.com/kvnloo/gz-sensors/commit/c0b3d1ca8065351ff804a32e3e3c5138532ef7b4) | See source carriers | **CHECK/LIMITED**, native Gazebo/Ogre2 integration or supported requirements missing. Preserve source authorship and avoid duplicate scopes. |

Current checked origin main at `8ddf4c17be8a434c51b51d5be7c866fb69aaa54f`. No product/sensor code changed and **no native CPU/CUDA/Ogre2 tests were executed** by this coordination migration. Recheck all heads, review and check runs before another promotion.

Credit: **AlessioLovato** reported camera depth/XYZ issue #614, **iche033** diagnosed/owns renderer correction, **kvnloo** authored #664; **ntfshard** contributed packed-LiDAR layout provenance (#493); preserve original wide-angle/DVL contributors and previous reviewers, with historical links below. No unsolicited mentions.

## Unmodified historical factory issue #147 — source archive

Original issue title: gz-sensors — canonical promotion queue & evidence index  
Original last modification: 2026-10-16T08:13:34Z  
Historical comments: 0 (none to migrate).  
Source: https://github.com/kvnloo/oss-factory/issues/147

**Historical policy and statuses below are quoted verbatim for provenance, NOT operative routing.** In particular, factory-local queues and Linear gates mentioned below were superseded by merged factory policy #130.

---

<!-- oss-factory:v1
{"id":"20261016-lane10-gz-sensors-promotion-queue-001","kind":"state","project":"gz-sensors","from":"chatgpt","to":["factory"],"status":"working","dedupe_key":"lane10:gz-sensors:canonical-promotion-queue","civ":{"city_id":"oss:gz-sensors"},"origin_url":"https://github.com/gazebosim/gz-sensors"}
-->

## Canonical promotion queue — Gazebo Sensors (Lane 10)

**Renderer-specific subproject tracking is [gazebosim/gz-rendering queue #153](https://github.com/kvnloo/oss-factory/issues/153)** (WATCH_ONLY / REGISTRY_PENDING); #147 contains only the cross-repo dependency and sensor-specific promotion work.
**Snapshot: 2026-10-16.** This is the single project-level promotion index for `gazebosim/gz-sensors` downstream work, kept in `kvnloo/oss-factory` because the registered `kvnloo/gz-sensors` fork has **Issues disabled** (`has_issues=false`). Its fork PRs/commits remain implementation/evidence carriers; the [factory-wide dashboard #14](https://github.com/kvnloo/oss-factory/issues/14) only summarizes readiness. Project routing is in [factory/projects.json](https://github.com/kvnloo/oss-factory/blob/main/factory/projects.json) (`id=gz-sensors`, `coordination_repo=kvnloo/gz-sensors`); this factory issue is an explicit Issues-disabled fallback, **not a second canonical project registry**.

**Confirmed new origin-ready publications: none.** Candidate work may be locally CPU-qualified without native Gazebo/renderer acceptance, review closure, current-head proof or operation-specific HITL. No worker slot, default-branch merge or upstream write is claimed here.

### Already live upstream (priority before any new contribution)

| Item | Latest observed state | Promotion decision |
|---|---|---|
| [gz-sensors #664](https://github.com/gazebosim/gz-sensors/pull/664) — depth camera intrinsics, author kvnloo | OPEN at `fff5fab51561a96ff63785a4a49b5dc6d6fcc19b`. [Maintainer iche033](https://github.com/gazebosim/gz-sensors/pull/664#issuecomment-6205266720) identified underlying Ogre2 renderer problem and verified #664's new test with [gz-rendering #1390](https://github.com/gazebosim/gz-rendering/pull/1390). Sep 25 Ubuntu Noble/Resolute GitHub check runs report success; an external Resolute Jenkins failure remains **not independently diagnosed**. | **LIVE_ORIGIN / HOLD_OWNER_DIRECTION.** Let the renderer owner land #1390 first; preserve #664 regression test and do not create another production sensor-side workaround without new requirement/owner agreement. [Fork QA #5](https://github.com/kvnloo/gz-sensors/pull/5) remains a HOLD/evidence mirror. |
| [gz-rendering #1390](https://github.com/gazebosim/gz-rendering/pull/1390) (cross-repo dependency, **not** a sensor PR) | OPEN at `0fad5d7b0bc4dcaed6fd2e3166aa85d0b221ef54`, owned by gazebosim maintainer. | **WAIT_OWNER / EXTERNAL_DEPENDENCY.** This project is not in the current factory registry and there is no verified `kvnloo/gz-rendering` fork; do not create a competing origin PR or claim its implementation. Lane 10's local test-only nonfinite-depth/XYZ, missing-Ogre2, projection and renderer-provenance harnesses remain **LIMITED** pending actual Ogre2 execution. |

### Existing fork PR carriers — all six indexed, none newly certified upstream-ready

| Fork code/evidence carrier | Current status / next proof |
|---|---|
| [#1 — O(1) sensor scheduling](https://github.com/kvnloo/gz-sensors/pull/1), `ef610504` | **LANDED/SUPERSEDED:** corresponding [origin #663](https://github.com/gazebosim/gz-sensors/pull/663) MERGED Oct 1. Do not promote again. |
| [#2 — wide-angle equidistant camera info](https://github.com/kvnloo/gz-sensors/pull/2), `0d0883b4` | **CHECK:** candidate for [origin issue #592](https://github.com/gazebosim/gz-sensors/issues/592). Four subsequent upstream commits were noted in the [factory dashboard](https://github.com/kvnloo/oss-factory/issues/14); require current-base native camera verification, contract, reviewers/ownership and HITL. |
| [#6 — authored projection translations](https://github.com/kvnloo/gz-sensors/pull/6), `662558f6` | **CHECK / STACKED on #2.** Preserve translation behavior and explicit credit; qualify as one coherent change or clearly separate invariant, but **do not promote the overlap twice**. |
| [#3 — deterministic DVL kinematics tests](https://github.com/kvnloo/gz-sensors/pull/3), `aab297c6` | **CHECK:** addresses [origin issue #648](https://github.com/gazebosim/gz-sensors/issues/648). Fresh upstream-head integration/unit evidence and owner/CI/HITL required. |
| [#4 — portable CTest results](https://github.com/kvnloo/gz-sensors/pull/4), `fd4873dd` | **LOCAL_ONLY / STACKED on #3.** Read-only evidence exporter; not a validated upstream sensor bug or independent promotion. |
| [#5 — #664 Resolute CI classification](https://github.com/kvnloo/gz-sensors/pull/5), `8802ec16` | **HOLD / QA_ONLY.** Keep baseline vs PR check distinctions; don't convert inconclusive external CI into a claim against #664. |

### Lane 10 experimental patches and reproducible evidence (not origin-ready)

| Workstream | Concrete carrier / evidence | Disposition |
|---|---|---|
| **CPU LiDAR packed fields / 18-byte record alignment** | [Published downstream commit `c0b3d1ca`](https://github.com/kvnloo/gz-sensors/commit/c0b3d1ca8065351ff804a32e3e3c5138532ef7b4); independent isolated GCC/Clang sanitizer/packing fixtures and synthetic 500k–600k point benchmarks reported in Lane 10 waves. ntfshard's [gz-sensors #493](https://github.com/gazebosim/gz-sensors/pull/493) establishes original packed-layout provenance. | **CHECK / CPU_FIXTURE_ONLY:** verify exact current sensor source, native CPU build/UBSan and row format semantics, conflict with existing PRs and supported impact. No GPU or native Gazebo result implied by fixtures. |
| **Point-cloud row padding / row_step, RGBA float aliasing, packed XYZ buffer handling** | Local code/patch handoffs from Lane 10 waves 12–16; synthetic RED/GREEN and sanitizers reported, but no new verified published fork heads for those corrections. | **LIMITED / UNPUBLISHED:** first consolidate non-overlapping patch versions and reproduce on actual native Gazebo pipeline. Do not open three independent overlapping PRs or cite inflated fixture counts as integration proof. |
| **Depth/XYZ camera equivalence and nonfinite comparisons** | Local test-only patches and GCC/Clang fixtures from Lane 10 waves 17–32; includes all-NaN false greens, finite-vs-infinite, camera3, and empty renderer cases. | **LIMITED / TEST_ONLY:** choose a single minimal invariant that actually survives real Ogre2 with [renderer #1390](https://github.com/gazebosim/gz-rendering/pull/1390). The owner-verified renderer fix outranks overlapping sensor-side production changes. |
| **Native/Ogre2 provenance and CI gate** | Local renderer/plugin detection and CI-evidence auditing scripts from Lane 10 waves 26–32. | **HOLD / NO GPU:** prove actual renderer loaded, device/version, executed test names, number of skips and exact revision. No claims from green CI summary alone. |

### Promotion admission / continuation
1. All future Lane 10 **gz-sensors** work and promotion decisions append dated canonical `oss-factory:v1` receipts **on this issue**. Existing PR-specific conversations remain the code/review evidence; **no second project promotion issue**, and no untracked queue in the fork.
2. For any candidate: pin source/target SHAs, reproduce supported requirement on the target native path (not just synthetic fixtures), prove RED/GREEN and adjacent regressions, check origin overlap, reviewers/CI and licensing, retain contributor attribution, and classify `CLEAN/CHECK/LIMITED/HOLD`. Only then mark **READY_FOR_HITL**; the **Linear Todo or authorized live-origin thread** remains required before origin-facing action.
3. Priority order: live #664 maintainer direction and CI → #2+#6 and #3 current-base tests → native packed LiDAR verification → standalone local sensor/perception experiments. Honor global six-worker claims; no slot claimed by this index.
4. **Credit:** iche033 diagnosed Ogre2 root cause and owns upstream renderer direction; kvnloo owns the sensor PR; ntfshard established LiDAR packing; original wide-angle/DVL contributors, reviewers and independent testers retain their authored contributions. No human GitHub mentions are emitted.

