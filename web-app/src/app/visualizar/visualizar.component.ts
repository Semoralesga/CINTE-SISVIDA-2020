import { Component, Input, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { CyclingTeam } from '../models/cycling-team.model';

@Component({
  selector: 'app-visualizar',
  templateUrl: './visualizar.component.html',
  styleUrls: ['./visualizar.component.scss'],
})
export class VisualizarComponent implements OnInit {
  idTeam: number;
  teamToshow: CyclingTeam;
  @Input() teams: CyclingTeam[];
  @Input() selectTeam: CyclingTeam;

  constructor(private location: Location) {}

  ngOnInit(): void {
    this.idTeam = this.selectTeam.id;
    console.log('>>Vis', this.teams);
    console.log('>> Team', this.selectTeam);
    this.teamToshow = this.teams.find((team) => team.id === this.selectTeam.id);
    console.log('>> Find', this.teamToshow);
    console.log('>>ID', this.idTeam);
  }

  goBack(): void {
    this.location.back();
  }

  nextTeam(): void {
    this.idTeam += 1;
    this.selectTeam = this.teams.find((team) => team.id === this.idTeam);
  }

  previousTeam(): void {
    this.idTeam -= 1;
    this.selectTeam = this.teams.find((team) => team.id === this.idTeam);
  }
}
