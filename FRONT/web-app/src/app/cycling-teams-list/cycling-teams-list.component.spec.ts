import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CyclingTeamsListComponent } from './cycling-teams-list.component';

describe('CyclingTeamsListComponent', () => {
  let component: CyclingTeamsListComponent;
  let fixture: ComponentFixture<CyclingTeamsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CyclingTeamsListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CyclingTeamsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
