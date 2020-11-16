import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CyclingTeam } from '../models/cycling-team.model';
import { ApiClientService } from '../services/api-client.service';

@Component({
  selector: 'app-especial',
  templateUrl: './especial.component.html',
  styleUrls: ['./especial.component.scss'],
})
export class EspecialComponent implements OnInit {
  teams: CyclingTeam[];
  selectTeam: CyclingTeam;
  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe((params) => {
      this.teams = JSON.parse(params['teams']);
      this.selectTeam = JSON.parse(params['selectTeam']);
    });
  }
}
