import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';

import { CyclingTeam } from '../models/cycling-team.model';

@Component({
  selector: 'app-add-edit-dialog',
  templateUrl: './add-edit-dialog.component.html',
  styleUrls: ['./add-edit-dialog.component.scss'],
})
export class AddEditDialogComponent implements OnInit {
  isEdit: boolean;
  form: FormGroup;
  team: CyclingTeam;
  title: string = 'Agregar Equipo';
  constructor(
    private fb: FormBuilder,
    private dialogRef: MatDialogRef<AddEditDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
    this.isEdit = data.isEdit;
    if (data.team) {
      this.team = data.team;
      this.title = 'Editar Equipo';
    }
  }

  ngOnInit(): void {
    this.createForm();
    if (this.isEdit) this.setValues();
  }

  private setValues(): void {
    this.name.setValue(this.team.name);
    this.victories.setValue(this.team.victories);
    this.cyclist_number.setValue(this.team.cyclist_number);
  }

  get name() {
    return this.form.get('name');
  }

  get victories() {
    return this.form.get('victories');
  }

  get cyclist_number() {
    return this.form.get('cyclist_number');
  }

  createForm(): void {
    this.form = this.fb.group({
      name: ['', Validators.required],
      victories: ['', Validators.required],
      cyclist_number: ['', Validators.required],
    });
  }

  close() {
    this.dialogRef.close();
  }

  save() {
    if (this.form.valid) {
      this.dialogRef.close(this.form.value);
    }
  }
}
