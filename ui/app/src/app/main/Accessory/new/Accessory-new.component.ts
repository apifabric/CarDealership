import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Accessory-new',
  templateUrl: './Accessory-new.component.html',
  styleUrls: ['./Accessory-new.component.scss']
})
export class AccessoryNewComponent {
  @ViewChild("AccessoryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}