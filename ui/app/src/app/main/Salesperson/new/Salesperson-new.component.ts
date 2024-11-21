import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Salesperson-new',
  templateUrl: './Salesperson-new.component.html',
  styleUrls: ['./Salesperson-new.component.scss']
})
export class SalespersonNewComponent {
  @ViewChild("SalespersonForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}