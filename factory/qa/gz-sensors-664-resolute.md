# QA: depth camera calibration PR #664 — Resolute build evidence

Status: **HOLD** (origin PR head `fff5fab51561a96ff63785a4a49b5dc6d6fcc19b`, checked 2026-10-12).

Origin: https://github.com/gazebosim/gz-sensors/pull/664
Requirement source: https://github.com/gazebosim/gz-sensors/issues/614 (reported by AlessioLovato).

## Observed facts

- The origin PR remains open and its code head is unchanged. On the current head, GitHub Actions for Bazel, Ubuntu, and package.xml succeeded; external Jenkins `gz_sensors-ci-pr_any-resolute-amd64` reports `failure` (run 25). External macOS Homebrew and Windows statuses are success.
- Independent comparison of unrelated origin heads shows the same failed Jenkins context: #639 (run 13), #658 (run 27), and #681 (run 40). These status values **do not identify which test or warning caused each result**.
- gz-sensors itself calls `gz_find_package(gz-rendering REQUIRED OPTIONAL_COMPONENTS ogre ogre2)` at CMakeLists.txt:65 on the PR head.
- Maintainers documented a **known main-branch CMake warning** on Ubuntu Resolute: the optional `gz-rendering-ogre` 11.0.0 component is absent after Ogre 1 was removed from packaging. This warning is reproduced verbatim on the main-branch build in gz-rendering#1346. See:
  - https://github.com/gazebosim/gz-rendering/issues/1346
  - https://github.com/gazebosim/gz-cmake/pull/587
  - https://discourse.openrobotics.org/t/gazebo-pmc-meeting-minutes-2026-09-28/58502
- The CMake fix is being worked on by existing maintainers (scpeters, j-rivero). Preserve their ownership; do not duplicate it or present our depth PR as the reason for the packaging change.
- Official Gazebo CI guidance says Jenkins marks builds yellow for **test failures or warnings** and red for infrastructure failures. A GitHub `failure` context does **not** establish one of these categories without the Jenkins report:
  https://gazebosim.org/docs/fortress/ci/

## Evidence missing — do not overstate

The exact Jenkins console/test report for #664 run 25 was inaccessible in this environment. We therefore **cannot** confirm whether the documented Ogre warning is the actual cause of this particular failed status, nor rule out a code/test regression. The v4/v5 synthetic USD geometry fixture is not a reproduction of Gazebo's Ogre/Ogre2 behavior.

## Small, independent next tasks

1. **CI discriminator (read-only):** obtain #664 run-25 console and `Test Result`/warnings; compare with same-period `gz_sensors-ci-main-resolute-amd64` and unrelated #681 run-40. Capture exact failing test/warning and whether it predates the candidate.
2. **Renderer correctness (fork-local):** run existing `DepthCameraIntrinsics` test on Ogre2 against both default and explicitly equivalent intrinsics. Compare full projection, depth, and XYZ across the same depth scene. Only run Ogre1 where the component exists; record a SKIP when it does not.
3. **Decision gate:** if the result is solely the documented upstream packaging/CMake warning, keep #664 scoped to the depth fix, don't patch `gz-cmake` here, and let #587 proceed under its own maintainer ownership. If a new #664-specific failure appears, isolate it with a minimal regression and source revision before proposing code.

## Author credit and scope

AlessioLovato: original depth/XYZ discrepancy (#614). scpeters and j-rivero: gz-cmake packaging-warning discussion and fix direction (#587); Gazebo PMC: CI baseline notes. Existing #664 authorship/test design remains unchanged.

No upstream write, merge, maintainer mention, renderer execution, or CI clearance is claimed by this record. This repository has GitHub Issues disabled, so this QA work is staged as a **draft fork PR** rather than opening a duplicate issue.
