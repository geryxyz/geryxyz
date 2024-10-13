---
title: Teaching at University of Szeged
permalink: /teaching
toc: false
---

## Hallgatóknak

<span class="center">
[<i class="fa-regular fa-comments"></i><br/>Fogadó óra](/teaching/consulting-hours){: .btn .btn--large .btn--edge}
[<i class="fa-solid fa-chalkboard-user"></i><br/>Kurzusok](/teaching/courses){: .btn .btn--large .btn--edge}
</span>

### Végzősöknek

{% assign theses_by_author = site.data.consultation.theses.theses | sort_natural: "author" %}
{% assign states = site.data.consultation.theses.states %}

{% assign in_progress_count = theses_by_author | where: "state", states.in_progress | size %} 

{% if in_progress_count < 8 %}
Vállalok szakdolgozat és diplomamunka vezetést.
{% else %}
Ebben a félévben már nem tudok több szakdolgozatot vagy diplomamunkát vállalni. Javaslom, hogy az érdeklődő hallgatók keressenek meg a következő félévben.
{% endif %}
Az egyes témákról és a részletekről az alábbi oldalakon található információ.

<span class="center">
[<i class="fa-solid fa-circle-info"></i><br/>Információk](/teaching/graduating/information){: .btn .btn--large .btn--edge}
[<i class="fa-regular fa-handshake"></i><br/>Jelentkezés](/teaching/graduating/applicant){: .btn .btn--large .btn--edge}
[<i class="fa-regular fa-comments"></i><br/>Konzultáció](/teaching/graduating/consultation){: .btn .btn--large .btn--edge}
[<i class="fa-solid fa-people-carry-box"></i><br/>Projektek](/teaching/graduating/projects){: .btn .btn--large .btn--edge}
[<i class="fa-solid fa-list"></i><br/>Témák](/teaching/graduating/topics){: .btn .btn--large .btn--edge}
</span>

Jelenleg {{ in_progress_count }} hallgatóval dolgozok együtt szakdolgozaton vagy diplomamunkán.

{% include thesis-student-table.liquid theses=theses_by_author state_filter=states.in_progress %}

## Érdeklődőknek

<span class="center">
[<i class="fa-solid fa-brain"></i><br/>Tanítási tapasztalatok](/teaching/experience){: .btn .btn--large .btn--edge}
[<i class="fa-solid fa-hands-holding-circle"></i><br/>Szakkörök](/teaching/study-groups){: .btn .btn--large .btn--edge}
</span>
