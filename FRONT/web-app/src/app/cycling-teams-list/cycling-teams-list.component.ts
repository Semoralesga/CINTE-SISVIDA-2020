import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { Observable } from 'rxjs';

import { ApiClientService } from '../services/api-client.service';

import { CyclingTeam } from '../models/cycling-team.model';
import { PageEvent } from '@angular/material/paginator';
import { AddEditDialogComponent } from '../add-edit-dialog/add-edit-dialog.component';
import { Router, NavigationExtras } from '@angular/router';

@Component({
  selector: 'app-cycling-teams-list',
  templateUrl: './cycling-teams-list.component.html',
  styleUrls: ['./cycling-teams-list.component.scss'],
})
export class CyclingTeamsListComponent implements OnInit {
  teams: CyclingTeam[] = [];
  teamsToShow: CyclingTeam[];

  pageSize: number = 10;
  pageIndex: number = 0;
  pageSizeOptions: number[] = [10, 20];

  filterControlDict = {
    name: true,
    id: true,
    cyclist: true,
    vic: true,
    date: true,
  };

  constructor(
    public apiClientService: ApiClientService,
    public dialog: MatDialog,
    public router: Router
  ) {}

  ngOnInit(): void {
    this.apiClientService.getTeams().subscribe((teams) => {
      this.teams = teams;
      this.sliceTeams();
    });
  }

  addTeam(): void {
    this.openAddEditTeamDialog(false);
  }

  editTeam(team: CyclingTeam): void {
    this.openAddEditTeamDialog(true, team);
  }

  removeTeam(teamId: number): void {
    console.log('>>Del', teamId);
    this.apiClientService.deleteTeam(teamId).subscribe((team) => {
      console.log('>> El equipo ha sido removido', team);
      this.reloadPage();
    });
  }

  reloadPage(): void {
    this.router
      .navigateByUrl('/', { skipLocationChange: true })
      .then(() => this.router.navigate(['/cycling_teams']));
  }

  openAddEditTeamDialog(isEdit: boolean, team?: CyclingTeam): void {
    const dialogConfig = new MatDialogConfig();
    const dataTeam = team ? team : undefined;
    dialogConfig.disableClose = true;
    dialogConfig.data = { isEdit: isEdit, team: dataTeam };

    const dialogRef = this.dialog.open(AddEditDialogComponent, dialogConfig);

    dialogRef.afterClosed().subscribe((form) => {
      console.log('>>form', form);
      const data = {
        name: form.name,
        victories: form.victories,
        cyclist_number: form.cyclist_number,
      };
      isEdit
        ? this.apiClientService
            .editTeam(dataTeam.id, data)
            .subscribe((team: CyclingTeam) => {
              console.log('>> El equipo ha sido editado', team);
              this.reloadPage();
            })
        : this.apiClientService
            .createTeam(data)
            .subscribe((team: CyclingTeam) => {
              console.log('>> El equipo ha sido creado', team);
              this.reloadPage();
            });
    });
  }

  filterTeams(pattern: string): void {
    console.log('>>Pat', pattern);
    if (pattern === 'id') {
      console.log('>. id');
      this.teams = this.teams.sort((a: CyclingTeam, b: CyclingTeam) =>
        this.filterControlDict['id'] === false
          ? a.id < b.id
            ? -1
            : +1
          : a.id > b.id
          ? -1
          : +1
      );
      this.filterControlDict['id'] = !this.filterControlDict['id'];
    } else if (pattern === 'name') {
      this.teams = this.teams.sort((a: CyclingTeam, b: CyclingTeam) =>
        this.filterControlDict['name'] === true
          ? a.name.toLowerCase() < b.name.toLowerCase()
            ? -1
            : +1
          : a.name.toLowerCase() > b.name.toLowerCase()
          ? -1
          : +1
      );
      this.filterControlDict['name'] = !this.filterControlDict['name'];
    } else if (pattern === 'vic') {
      this.teams = this.teams.sort((a: CyclingTeam, b: CyclingTeam) =>
        this.filterControlDict['vic'] === true
          ? a.victories < b.victories
            ? -1
            : +1
          : a.victories > b.victories
          ? -1
          : +1
      );
      this.filterControlDict['vic'] = !this.filterControlDict['vic'];
    } else if (pattern === 'cyclist') {
      this.teams = this.teams.sort((a: CyclingTeam, b: CyclingTeam) =>
        this.filterControlDict['cyclist'] === true
          ? a.cyclist_number < b.cyclist_number
            ? -1
            : +1
          : a.cyclist_number > b.cyclist_number
          ? -1
          : +1
      );
      this.filterControlDict['cyclist'] = !this.filterControlDict['cyclist'];
    }
    this.sliceTeams();
  }

  paginationEvent(event: PageEvent): void {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    console.log('>>Page', this.pageIndex, this.pageSize);
    this.sliceTeams();
  }

  sliceTeams() {
    this.teamsToShow = this.teams.slice(
      this.pageIndex * this.pageSize,
      this.pageSize * (this.pageIndex + 1)
    );
    console.log('>Teams', this.teams);
  }

  goDetail(team: CyclingTeam): void {
    console.log('1212', team);
    const extras: NavigationExtras = { state: team };
    this.router.navigate([`cycling_teams/detail`], {
      queryParams: {
        teams: JSON.stringify(this.teams),
        selectTeam: JSON.stringify(team),
        skipLocationChange: true,
      },
    });
  }
}
